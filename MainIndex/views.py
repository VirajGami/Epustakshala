from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.http import HttpResponse
from . import views
from Cart.models import Cart , Order
from Registration.models import Customer
# Create your views here.

Customer_session_nm = None
Customer_session_id = None
order = None
carts = None

def index(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    Books=Book.objects.all()
    Authors=Author.objects.all()
    Publications=Publication.objects.all()
    Categorys=Category.objects.all()
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Books=Books.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm  , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':Books})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    
        return render(request,'index.html',{'Books':Books,'Authors':Authors,'Publications':Publications,'Categorys':Categorys, 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize() })   
    return render(request,'index.html',{'Books':Books,'Authors':Authors,'Publications':Publications,'Categorys':Categorys,})   
    
   


def CategoryView(request, id):
    Customer_session_nm = None
    Customer_session_id = None
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
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    CategoryValue = Category.objects.get(id=id)
    allBook = Book.objects.all()
    Books = Book.objects.filter(Category=CategoryValue)
    Name = Category.objects.get(id=id).CategoryName
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        foundBooks=allBook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':foundBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':foundBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'ShowBooks.html', {'Books':Books, 'Name':Name, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request, 'ShowBooks.html', {'Books':Books, 'Name':Name})

def PublicationView(request, id):
    Customer_session_nm = None
    Customer_session_id = None
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
    PublicationValue = Publication.objects.get(id=id)
    Books = Book.objects.filter(Publication=PublicationValue)
    Name = Publication.objects.get(id=id).PublicationName
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Boo = Book.objects.all()
        Books=Boo.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':Books})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'showPublication.html', {'Books':Books, 'Name':Name , 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request, 'showPublication.html', {'Books':Books, 'Name':Name })

def AuthorView(request, id):
    Customer_session_nm = None
    Customer_session_id = None
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
    Books= Book.objects.all()
    # bname=request.GET.get('Bookname')
    # if bname!='' and bname is not None:
    #     Books=Books.filter(BookName__icontains= bname)
    #     return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})   
    AuthorValue = Author.objects.get(id=id)
    Books = Book.objects.filter(Author=AuthorValue)
    Name = Author.objects.get(id=id).AuthorName
    desc = Author.objects.get(id=id).AuthorDesc
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Boo = Book.objects.all()
        Books=Boo.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':Books})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'ShowAuthor.html', {'Books':Books, 'Name':Name,'desc':desc , 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})   
    return render(request, 'ShowAuthor.html', {'Books':Books, 'Name':Name,'desc':desc })    


def SearchView(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    Books= Books.objects.all()
    Authors=Author.objects.all()
    Publications=Publication.objects.all()
    Categorys=Category.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        Books=Books.filter(BookName__icontains= bname)
        return render(request,'ShowSearch.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm ,  'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})   
    return render(request, 'ShowSearch.html', {'Books':Books})


    
def DetailsView(request,id):
    Customer_session_nm = None
    Customer_session_id = None
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
    Detailsbook=Book.objects.all()
    Books=Book.objects.get(id=id)
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'product-detail.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request, 'product-detail.html',{'Books':Books})


def contact(request):
    if request.method == 'POST':
        Fullname = request.POST.get('fullname','')
        email   = request.POST.get('email','')
        phone  = request.POST.get('phone','')
        message = request.POST.get('message','')
        c=Contact(FullName=Fullname, Email=email, Phone=phone , Message=message)
        c.save()
        print("saved")
    return render(request,'Contact/contactform.html',{})

def got(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    Detailsbook=Book.objects.all()
    Books = Book.objects.filter(SubCategory="GOT")
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'gameofthrones.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    
    return render(request,'gameofthrones.html',{'Books':Books})

def hp(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    Detailsbook=Book.objects.all()
    Books = Book.objects.filter(SubCategory="HP")
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'harrypotter.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    
    return render(request, 'harrypotter.html', {'Books':Books})

def tw(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    Detailsbook=Book.objects.all()
    Books = Book.objects.filter(SubCategory="TW")
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'twilight.html',{'Books':Books, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request, 'twilight.html', {'Books':Books})

def About(request):

    return render(request , 'aboutus.html' , {})


def allBooks(request):
    Customer_session_nm = None
    Customer_session_id = None
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
    book = Book.objects.all()
    cat = Category.objects.all()
    Detailsbook=Book.objects.all()
    Books = Book.objects.filter(SubCategory="TW")
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    bname=request.GET.get('Bookname')
    if bname!='' and bname is not None:
        searchBooks=Detailsbook.filter(BookName__icontains= bname)
        if request.session.has_key('name'):
            Customer_session_nm=request.session['name']
            return render(request,'ShowSearch.html',{'Books':searchBooks, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
        else:
            return render(request,'ShowSearch.html',{'Books':searchBooks})
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request, 'allBooks.html',{'Books':book, 'Customer_session_nm':Customer_session_nm , 'order':order , 'carts':carts , 'category':cat, 'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request, 'allBooks.html', {'category':cat, 'Books':book })