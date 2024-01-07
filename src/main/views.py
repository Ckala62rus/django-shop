from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title" : "Home - Главная страница",
        "content" : "Магазин мебели HOME",
    }
    return render(request, template_name="main/index.html", context=context)

def about(request: WSGIRequest):
    context = {
        "title": "Home - Главная страница",
        "content": "Коротко о нас",
        "about_text": "Мы тестовый интернет магазин"
    }
    return render(request, template_name="main/about.html", context=context)