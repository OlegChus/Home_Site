from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Home',
        'content': 'Store HOME',
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('About page')
