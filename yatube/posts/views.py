from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import DEF_NUM_POSTS
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User = get_user_model()

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, DEF_NUM_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).all().order_by('-pub_date')
    paginator = Paginator(post_list, DEF_NUM_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    post_list = Post.objects.filter(
        author__username=username).order_by('-pub_date')
    paginator = Paginator(post_list, DEF_NUM_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    author = get_object_or_404(User, username=username)
    num_of_posts = Post.objects.filter(author__username=username).count()

    context = {
        'page_obj': page_obj,
        'author': author,
        'num_of_posts': num_of_posts,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    num_of_posts = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'num_of_posts': num_of_posts,
    }
    return render(request, 'posts/post_detail.html', context)
