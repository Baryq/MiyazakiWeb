from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from .models import Anime

nav = [
    {'name': 'index', 'text': 'Главная страница'},
    {'name': 'about', 'text': 'О сайте'},
    {'name': 'biography', 'text': 'Биография автора'},
    {'name': 'works', 'text': 'Работы автора'}
]


def index(request):
    context = {'title': 'Главная страница', 'nav': nav}
    return render(request, 'anime/index.html', context)


def biography(request):
    context = {'title': 'Биография автора', 'nav': nav}
    return render(request, 'anime/biography.html', context)


def works(request):
    all_works = Anime.objects.all()
    return render(request, 'anime/works.html', {'all_works': all_works})


def work_no(request, no):
    limit = 43  # maximum number of works
    if no > limit:
        url = reverse('works')
        return HttpResponseRedirect(url)
    else:
        work = Anime.objects.get(pk=no)
        return render(request, 'anime/base_work.html', {'work': work})


def contacts(request):
    context = {'title': 'Контакты', 'nav': nav}
    return render(request, 'anime/contacts.html', context)


def not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')
