from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from goods.models import Products


# Create your views here.

def catalog(request, category_slug: str) -> HttpResponse:

    page = request.GET.get('page', 1)

    if category_slug.lower() == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Каталог",
        "content": "Магазин мебели HOME",
        "goods": current_page,
        "slug_url": category_slug
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
