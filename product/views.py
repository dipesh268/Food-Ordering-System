from django.shortcuts import render,redirect
from product.models import *
# Create your views here.


def home(request):
    return render(request, "index.html")


def login_page(request):
    return render(request,'login.html')
    