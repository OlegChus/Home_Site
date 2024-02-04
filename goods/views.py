from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Goods/Catalog',
        'content': 'GOODS/Catalog',
    }

    return render(request, 'goods/catalog.html', context=context)


def product(request):
    context = {
        'title': 'GOODS/Product',
        'content': 'GOODS/Product',
    }

    return render(request, 'goods/product.html', context=context)
