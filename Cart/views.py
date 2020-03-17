
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from Registration.models import Customer

from .models import *
import os
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import datetime
import time
import smtplib
import pymysql.cursors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from datetime import date
# Create your views here.

Customer_session_nm = None
Customer_session_id = None
order = None
carts = None
  
def CartView(request):
    Customer_session_nm = None
    Customer_session_id = None
    order =None
    carts = None
    Books = Book.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            user = Customer_session_id
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Books=Books.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':Books})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        Customer_session_id = None
        if request.session.has_key('id'):
            Customer_session_id=request.session['id']
        user = Customer_session_id

        carts = Cart.objects.filter(user=user)
        orders = Order.objects.filter(user=user)
        if carts.exists():
            print("if")
            if orders.exists():
                print("if if ")
                order = orders[0]
                return render(request, 'cart.html', {'carts': carts, 'order': order , 'Customer_session_nm':Customer_session_nm , 'name':Customer.objects.get(id=user).CustomerName.capitalize() })
            else:
                return render(request,'cart.html' ,{ 'carts': carts, 'order': order , 'Customer_session_nm':Customer_session_nm  , 'name':Customer.objects.get(id=user).CustomerName.capitalize()} )
                # messages.warning(request, "You do not have any item in your Cart")

            
        else:
            print('else')
            # messages.warning(request, "You do not have any item in your Cart")
            return render(request,'cart.html' ,{ 'carts': carts, 'order': order ,'Customer_session_nm':Customer_session_nm , 'name':Customer.objects.get(id=user).CustomerName.capitalize()} )
    else:
        return redirect("Registration:Login")



def add_to_cart(request, id):
    
    # Customerfds = Customer.objects.get(id=15)
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        if request.session.has_key('id'):
            Customer_session_id=request.session['id']
        userid = Customer_session_id
        item = get_object_or_404(Book, id=id)
        Customer_name=Customer.objects.get(id=userid)
        order_item, created = Cart.objects.get_or_create(
            item=item,
            user=Customer_name
        )
        order_qs = Order.objects.filter(user=userid)
        if order_qs.exists():
            order = order_qs[0]
            print('order if')
            # check if the order item is in the order
            if order.orderitems.filter(item__id=item.id).exists():
                print('order if if')
                order_item.quantity += 1
                updatestock(userid)
                order_item.save()
                # messages.info(request, f"{item.BookName} quantity has updated.")
                return redirect("Cart:CartView")
            else:
                
                order.orderitems.add(order_item)
                updatestock(userid)
                # messages.info(request, f"{item.BookName} has added to your cart.")
                return redirect("Cart:CartView")
        else:
            order = Order.objects.create(user=Customer_name)
            order.orderitems.add(order_item)
            # messages.info(request, f"{item.BookName} has added to your cart.")
            return redirect("Cart:CartView")
    else:
        return redirect("Registration:Login")

def remove_from_cart(request, id):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
    userid = Customer_session_id
    Customer_name=Customer.objects.get(id=userid)
    item = get_object_or_404(Book, id=id)
    cart_qs = Cart.objects.filter(user=Customer_name , item=item)

    
    
    
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=Customer_name)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=Customer_name,
            )[0]
            order_item.delete()
            # messages.warning(request, "This item was removed from your cart.")
            return redirect("Cart:CartView")
        else:
            # messages.warning(request, "This item was not in your cart")
            return redirect("Cart:CartView")
    else:
        # messages.warning(request, "You do not have an active order")
        return redirect("MainIndex:index")


def decreaseCart(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
    userid = Customer_session_id
    Customer_name=Customer.objects.get(id=userid)
    item = get_object_or_404(Book, id=id)
    order_qs = Order.objects.filter(
        user=Customer_name
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=Customer_name
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                updatestockdes(userid)
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                updatestockdes(userid)
                order_item.delete()
                # messages.warning(request, f"{item.BookName} has removed from your cart.")
            # messages.info(request, f"{item.BookName} quantity has updated.")
            return redirect("Cart:CartView")
        else:
            # messages.info(request, f"{item.BookName} quantity has updated.")
            return redirect("Cart:CartView")
    else:
        # messages.info(request, "You do not have an active order")
        return redirect("MainIndex:index")


def Checkout(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    else:
        return redirect('MainIndex:index')
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
        user = Customer_session_id
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    userid = Customer_session_id 
    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user)
    Customer_obj = Customer.objects.get(id=userid)
    if carts.exists():
        print("if")
        if orders.exists():
            print("if if ")
            order = orders[0]
        else:
            order = None
            carts = None
            return redirect("MainIndex:index")
    else:
        order = None
        carts = None
        return redirect("MainIndex:index")
    if request.method=='POST':
        firstname=request.POST.get('Billingfirst','')
        lastname=request.POST.get('Billinglast','')
        address = request.POST.get('firstaddress','')
        address2 = request.POST.get('secondaddress','')
        pincode = request.POST.get('pincode','')
        state = request.POST.get('state','')
        city = request.POST.get('city','')
        Cus = Customer.objects.get(id=user)
        Cus.CustomerAddress = address
        Cus.CustomerAddress2 = address2
        Cus.CustomerPincode  = pincode
        Cus.BillingFirstName = firstname
        Cus.BillingLastName = lastname
        Cus.CustomerState = state
        Cus.CustomerCity = city
        Cus.save()
        createpdf(userid)
        # updatestock(userid)
        try:
            sendbill(Cus.CustomerEmail)
        except:
            print('error sending mail')
        return redirect("Cart:invoice")

    
    Detailsbook=Book.objects.all()
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'user':Customer_obj,'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    return render(request , 'Checkout.html' , { 'carts': carts, 'order': order , 'Customer_session_nm':Customer_session_nm , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})





def createpdf(Customer_session_id):
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
    canvas1 =canvas.Canvas("(" + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + ").pdf", pagesize=letter)
    # canvas1 =canvas.Canvas("C:/Users/Neive/Desktop/py/ hello.pdf", pagesize=letter)
    # canvas1.setFillColorRGB(255,210,150)
    canvas1.setLineWidth(.3)
    canvas1.setFont('Helvetica', 12)
    canvas1.line(50, 747, 580, 747) #FROM TOP 1ST LINE
    canvas1.drawString(280, 750, "Bill")
    canvas1.drawString(60, 720, "COMPANY NAME:- E-Pustakshala")
    canvas1.drawString(60, 690, "EMAIL-ID:- Nevilbavarva477@gmail.com")
    canvas1.drawString(60, 660, "ADDRESS:- abc,def,360005-rajkot")
    canvas1.drawString(450, 720, "DATE :- " + datetime.datetime.now().strftime("%d/%m/%y"))
    canvas1.line(450, 710, 560, 710)
    canvas1.line(50, 640, 580, 640)#FROM TOP 2ST LINE
    canvas1.line(50, 748, 50, 50)#LEFT LINE
    canvas1.line(400, 640, 400, 50)# MIDDLE LINE
    canvas1.line(580, 748, 580, 50)# RIGHT LINE
    canvas1.drawString(475, 615, 'TOTAL AMOUNT')
    canvas1.drawString(100, 615, 'PRODUCT')
    canvas1.line(50, 600, 580, 600)#FROM TOP 3rd LINE
    lines = 550
    for cart in carts:  
        canvas1.drawString(60, lines, cart.item.BookName)
        canvas1.drawString(500, lines, str(cart.item.BookPrice))
        lines = lines -  50
    TOTAL = order.get_totals()
    print(TOTAL)
    canvas1.line(50, 100, 580, 100)#FROM TOP 4th LINE
    canvas1.drawString(60, 80, " TOTAL AMOUNT ")
    canvas1.drawString(500, 80, str(TOTAL))
    canvas1.line(50, 50, 580, 50)#FROM TOP LAST LINE
    canvas1.save()
    print('executed !!')


def sendbill(email):
    COMMASPACE = ', '
    sender = 'nevilbavarva477@gmail.com'
    gmail_password = 'tnchihokkrrjosee'
    recipients = [str(email)]

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = ' E-Pustakshala (Order Placed)'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer['body'] = '\n Visit : e-pustakshala.herokuapp.com/contact for any query'
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = [str("(" + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + ").pdf")]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise
    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise



def updatestock(Customer_session_id):
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
    for cart in carts:  
        refBooks = Book.objects.get(BookName=cart.item.BookName)
        print("before call : " + str(refBooks.BookStock))
        if(refBooks.BookStock < 1):
            refBooks.BookStock == 0
            print('value is less than zero')
        else: 
            refBooks.BookStock -= 1
            refBooks.save()
            print("after call : " + str(refBooks.BookStock))


def updatestockdes(Customer_session_id):
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
    for cart in carts:  
        refBooks = Book.objects.get(BookName=cart.item.BookName)
        print("before call : " + str(refBooks.BookStock)) 
        refBooks.BookStock += 1
        refBooks.save()
        print("after call : " + str(refBooks.BookStock))


def invoice(request):
    Customer_session_nm = None
    Customer_session_id = None
    order =None
    carts = None
    Books = Book.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        if request.session.has_key('id'):
                Customer_session_id=request.session['id']
                user = Customer_session_id
        carts = Cart.objects.filter(user=user)
        orders = Order.objects.filter(user=user)
        CustomerName = Customer.objects.get(id=Customer_session_id)
        if carts.exists():
            if orders.exists():
                order = orders[0]
            else:
                order = None
                carts = None
        else:
            order = None
            carts = None          
        return render(request,'invoice.html', {'carts': carts, 'order': order , 'Customer':CustomerName})
    else:
        return redirect("Registration:Login")
    return redirect("MainIndex:index")


    