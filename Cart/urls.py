from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('Home/Cart/', views.CartView , name="CartView"),
    path('Home/Cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('Home/Cart/Remove/<int:id>', views.remove_from_cart , name="remove_from_cart"),
    path('Home/Cart/Delete/<int:id>', views.decreaseCart , name="decreaseCart"),
    path('Home/Cart/Checkout', views.Checkout , name="Checkout"),
    path('Home/Cart/invoice', views.invoice , name="invoice"),
]