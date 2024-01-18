from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request: HttpResponse) -> HttpResponse:
    context = {
        'title': 'Home - Авторизация',
    }
    return render(
        request,
        template_name="users/login.html",
        context=context
    )


def registration(request: HttpResponse) -> HttpResponse:
    context = {
        'title': 'Home - Регистрация',
    }
    return render(
        request,
        template_name="users/registration.html",
        context=context
    )


def profile(request: HttpResponse) -> HttpResponse:
    context = {
        'title': 'Home - Кабинет',
    }
    return render(
        request,
        template_name="users/profile.html",
        context=context
    )


def logout(request: HttpResponse) -> HttpResponse:
    context = {
        'title': 'Home - Выход',
    }
    return render(
        request,
        '',
        context
    )
