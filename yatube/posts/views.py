from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import DEF_NUM_POSTS

# Главная страница
# last var of ordering in the views
# for index posts = Post.objects.order_by('-pub_date')[:10]
# for group_posts posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

def index(request):
    posts = Post.objects.all()[:DEF_NUM_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:DEF_NUM_POSTS]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)
