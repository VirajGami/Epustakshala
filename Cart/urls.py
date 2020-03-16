from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('Cart/', views.CartView , name="CartView"),
    path('Cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('Cart/Remove/<int:id>', views.remove_from_cart , name="remove_from_cart"),
    path('Cart/Delete/<int:id>', views.decreaseCart , name="decreaseCart"),
    path('Cart/Checkout', views.Checkout , name="Checkout"),
    path('Cart/invoice', views.invoice , name="invoice"),
]