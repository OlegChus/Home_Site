from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Наши контакты',
        'text_on_page': 'Наши работы :'
    }

    return render(request, 'main/about.html', context=context)
