from django.shortcuts import render,redirect
from product.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.


def home(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        customer_email = request.POST.get('Email')
        password = request.POST.get('password')
        print(password)
        print(customer_email)
        
        if customer.objects.filter(customer_email=customer_email).exists():
            user = authenticate(customer_email=customer_email, password=password)
            if user is None:
                messages.info(request, "Invalid password.")
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('/index/')
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



    