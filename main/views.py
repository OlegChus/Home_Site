from django.shortcuts import render

from goods.models import Categories


# Create your views here.


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Наши контакты',
        'text_on_page': 'Наши работы :'
    }

    return render(request, 'main/about.html', context=context)
