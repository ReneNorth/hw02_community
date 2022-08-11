from django.shortcuts import render, get_object_or_404
#from django.urls import path
#from . import views
from .models import Post, Group



# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # другие способы получить посты (а как делать пагинацию?)
    # posts = Post.objects.order_by('-pub_date')[:10]
    # Post.objects.get(id=1)
    # Post.objects.filter(pub_date__year=1854 
    # Post.objects.filter(text__startswith='Писать не хочется')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)

# Create your views here.

def group_list(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)
