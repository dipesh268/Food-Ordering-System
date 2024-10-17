from django.shortcuts import render,redirect
from product.models import *
from django.contrib import messages
from product.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

#for Home page logic...
def home(request):
     
    item1 = product_list.objects.filter(product_type__product_type ='Rajasthan Food')
    item2 = product_list.objects.filter(product_type__product_type ='south Indian Food')
    
    if request.GET.get('search'):
        item_list=''
        item_list = product_list.objects.filter(
            Q(prodct_name__icontains = request.GET.get('search')) |
            Q(prodct_type__icontains = request.GET.get('search')) |
            Q(prodct_price__icontains = request.GET.get('search')) |
            Q(product_Description__icontains = request.GET.get('search'))
            )
        
        
    return render(request, "index.html",context={'item1':item1,'item2':item2})

#product contant details...
def item_view_page(request,id):
    #only one record get from DB that's why use GET
    queryset = product_list.objects.get(id=id)
    return render(request,'item_view.html',context={'recipe':queryset})



#Login page backend code....
def login_page(request):
    if request.method == "POST":
        #store the value from the login page
        customer_email = request.POST.get('Email')
        pwd = request.POST.get('pwd')
        #print(customer_email) check the email is get from form 
        #print(pwd) check the password is get from form
        
        #check the email is valid or not 
        if customer.objects.filter(customer_email=customer_email).exists():
            #check the password is valid or not 
            user = authenticate(customer_email=customer_email,password=pwd)
            #print(user1) is for check the code is run or not
            print(user)
            if user:
                #if user is valid than login in main page
                login(request,user)
                return redirect('/')
            else:
                #if passowrd is wrong than through the message
                messages.info(request, "Invalid password.")
                return redirect('/login/')
        else:
            #if email is wrong than through the message
            messages.info(request, "Invalid Username.")
            return redirect('/login/')
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


#Register code...
def register_page(request):
    #check the method of form in template
    if request.method == "POST":
        #store the value in var.
        data = request.POST
        frist_name=data.get('frist_name')
        last_name=data.get('last_name')
        email=data.get('email')
        gender=data.get('inlineRadioOptions')
        phno=data.get('phno')
        password=data.get('password')
        address=data.get('addr')
        pincode=data.get('pincode')
        #save in the db table model.
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
        #if register done then throw into login page
        return redirect('/login/')
    return render(request,'register.html')

@login_required(login_url="/login/")
def add_to_cart(request,id):
    product = product_list.objects.get(id=id)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user=user,is_paid = False)

    CartItem = CartItems.objects.create(cart = cart,product = product)
    return redirect(request.META.get('HTTP_REFERER'))
    # if request.method == "POST":
    #     data = request.POST
    #     product_name = data.get('p_name')
    #     print(product_name)
    #     queryset = product_list.objects.get(prodct_name = product_name)
    #     print(queryset)
    #     return product_name
    # item = product_list.objects.get(id=id)
    # user = request.user
    # carts = cart.objects.create(
    #     user = user,
    #     prodct_name = item.prodct_name,
        
    # )
