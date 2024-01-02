from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse("Home page")
    context = {
        "title" : "Home",
        "content" : "Lorem ipsum dollar sit amet",
    }
    return render(request, template_name="index.html", context=context)

def about(request: WSGIRequest):
    return HttpResponse("About page")