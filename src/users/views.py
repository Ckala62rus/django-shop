from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm


# Create your views here.

def login(request: WSGIRequest) -> HttpResponse:

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
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
