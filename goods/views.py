from django.shortcuts import render, get_list_or_404
from .models import Categories, Products


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(
            category__slug=category_slug))

    context = {
        'title': 'Home - Catalog',
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):
    product_card = Products.objects.get(slug=product_slug)

    context = {
        'title': product_card.name,
        'product': product_card,
    }

    return render(request, 'goods/product.html', context=context)
