from django.shortcuts import render, get_list_or_404

from goods.models import Products


# Create your views here.

def catalog(request, category_slug: str):
    if category_slug.lower() == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Каталог",
        "content": "Магазин мебели HOME",
        "goods": goods
    }
    return render(
        request,
        template_name='goods/catalog.html',
        context=context
    )

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product' : product
    }
    return render(
        request,
        template_name='goods/product.html',
        context=context
    )
