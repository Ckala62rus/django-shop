from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        "title": "Каталог",
        "content": "Магазин мебели HOME",
    }
    return render(request, template_name='goods/catalog.html', context=context)

def product(request):
    return render(request, template_name='goods/product.html')