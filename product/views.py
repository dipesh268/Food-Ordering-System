from django.shortcuts import render,redirect
from product.models import *
from django.contrib import messages
from product.models import user
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


def home(request):
    item_list = product_list.objects.all()
    
    if request.GET.get('search'):
        item_list = item_list.filter(
            Q(prodct_name__icontains = request.GET.get('search')) |
            Q(prodct_type__icontains = request.GET.get('search')) |
            Q(prodct_price__icontains = request.GET.get('search')) |
            Q(product_Description__icontains = request.GET.get('search'))
            )
        
    return render(request, "index.html",context={'items':item_list})


def login_page(request):
    if request.method == "POST":
        customer_email = request.POST.get('Email')
        pwd = request.POST.get('pwd')
        print(pwd)
        print(customer_email)
        
        if user.objects.filter(customer_email=customer_email).exists():
            user1 = authenticate(customer_email=customer_email,password=pwd)
            print(user1)
            if user:
                login(request,user1)
                return redirect('/')
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
        user.objects.create(
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



    