from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')


def index1(request):
    return render(request, 'home/index1.html')


def index2(request):
    return render(request, 'home/index2.html')


def index3(request):
    return render(request, 'home/index3.html')


def index4(request):
    return render(request, 'home/index4.html')