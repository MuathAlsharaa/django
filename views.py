from cgitb import Hook
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    Home = {
        'book':Book.objects.all()
    }
    return render(request,'pages/index.html',Home)

def test(request):
    return render(request,'test.html')

# def SH(request):
    # return render(request,'pages/index.html')

def book(request):
    return render(request,'pages/books.html')


def delets(request):
    return render(request,'pages/delete.html')


def uptades(request):
    return render(request,'pages/uptade.html')