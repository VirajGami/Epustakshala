from django.shortcuts import render , redirect
import os
from MainIndex.models import *
from .models import *
from MainIndex.views import *
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
import smtplib
from django.contrib import messages



Customer_session_nm = None
Customer_session_id = None
total = 0
def Login(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
        print(Customer_session_id)
    user = Customer_session_id

    if request.method=='POST':   
        username=request.POST['username']
        password=request.POST['password']
        Books=Book.objects.all()
        Authors=Author.objects.all()
        Publications=Publication.objects.all()
        Categorys=Category.objects.all()
        bname=request.GET.get('Bookname')
        if bname!='' and bname is not None:
            Books=Books.filter(BookName__icontains= bname)
            return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm})
        
        Customer_name=Customer.objects.filter(CustomerName__contains=username,CustomerPassword__contains=password).values_list('CustomerName', 'id').first()
        if Customer_name is not None:
            request.session['name'] = Customer_name
            request.session['id'] = Customer_name[1]
            return redirect('Registration:cust_login1')
        else:
           
            return render(request,'LoginRegister/login.html',{})
    return render(request,'LoginRegister/Login.html',{})

# 
# username contstraint error (unique)- display error in login form
# 



def Register(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.method == 'POST':
        CustomerName= request.POST.get('username','')
        CustomerEmail= request.POST.get('email','')
        CustomerPassword = request.POST.get('password1','')
        c=Customer(CustomerName=CustomerName, CustomerPassword=CustomerPassword, CustomerEmail=CustomerEmail)
        c.save()
        try:
            sendmail(CustomerEmail, CustomerName)
        except:
            print("except")
            return redirect('Registration:Login')
        print("normal")
        # return render(request, 'LoginRegister/Login.html', {})
        return redirect('Registration:Login')
    return render(request, 'LoginRegister/Register.html', {})
    

def cust_login1(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
   
    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user)
    if carts.exists():
        print("if")
        if orders.exists():
            print("if if ")
            order = orders[0]
        else:
            order = None
            carts = None
    else:
        order = None
        carts = None
    Books=Book.objects.all()
    Authors=Author.objects.all()
    Publications=Publication.objects.all()
    Categorys=Category.objects.all()
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Books=Books.filter(BookName__icontains= bname)
        return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts})

    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']

    else:
        return render(request,'LoginRegister/Login.html',{})
    return render(request,'index.html',{'Books':Books,'Authors':Authors,'Publications':Publications,'Categorys':Categorys, 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})   


def Logout(request):
    try:
        del request.session['name']
        return redirect('MainIndex:index',)
    except:
      pass
    return redirect('MainIndex:index')



# 
# 
# 
# for sending registration mail
def sendmail(CustomerEmail , CustomerName):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nevilbavarva477@gmail.com','tnchihokkrrjosee')
    # server =smtplib.SMTP('smtp.gmail.com',587)
    # server.ehlo()
    # server.starttls()
    # server.ehlo()
    # server.login('nevilbavarva477@gmail.com','tnchihokkrrjosee')
    email = CustomerEmail
    name = CustomerName

    subject ='Registration'
    body= 'Dear ' + str(name) +' ,'+ '\n Thanks for you Registration in E-Pustakshala. Your account has been successfully created.'

    msg=f"subject:{subject}\n\n{body}"

    server.sendmail(
        'nevilbavarva477@gmail.com',
        email,
        msg

    )
    print('msg has been send')
    server.quit()

