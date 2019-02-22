from django.shortcuts import render
from django.http import HttpResponse


# Default
def blank(request):
    return HttpResponse('choose a path: index, base, about')


# calling each webpage base on path
def index(request):
    return render(request, 'cwApp/index.html')


def base(request):
    return render(request, 'cwApp/base.html')


def about(request):
    return render(request, 'cwApp/about.html')
