from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


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


def registration(request: WSGIRequest) -> HttpResponse:

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }

    return render(
        request,
        template_name="users/registration.html",
        context=context
    )


@login_required
def profile(request: WSGIRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'form': form
    }

    return render(
        request,
        template_name="users/profile.html",
        context=context
    )


@login_required
def logout(request: WSGIRequest) -> HttpResponse:
    auth.logout(request)
    return redirect(reverse('main:index'))
