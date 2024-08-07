from django.shortcuts import render,redirect
from product.models import *
from django.contrib import messages
from product.models import customer
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        customer_email = request.POST.get('Email')
        pwd = request.POST.get('pwd')
        print(pwd)
        print(customer_email)
        
        if customer.objects.filter(customer_email=customer_email).exists():
            user = customer.objects.filter(password = pwd)
            print(user)
            if user:
                login(request,user)
                return redirect('/index/')
            else:
                messages.info(request, "Invalid password.")
                return redirect('/login/')
        else:
            messages.info(request, "Invalid Username.")
            return redirect('/login/')
        
    return render(request,'login.html')


def register_page(request):
    if request.method == "POST":
        data = request.POST
        frist_name=data.get('frist_name')
        last_name=data.get('last_name')
        email=data.get('email')
        gender=data.get('inlineRadioOptions')
        phno=data.get('phno')
        password=data.get('password')
        address=data.get('addr')
        pincode=data.get('pincode')
        customer.objects.create(
            customer_F_name  = frist_name,
            customer_L_name = last_name,
            customer_mobile_no = phno,
            customer_address = address,
            customer_pincode = pincode,
            customer_gender = gender,
            customer_email = email,
            password = password
        )
        return redirect('/login/')
    return render(request,'register.html')



    