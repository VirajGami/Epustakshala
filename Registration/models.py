from django.db import models
from MainIndex.models import *

# class WishList(models.Model):
#     # WishCustomer = models.ForeignKey(Customer , on_delete=models.SET_DEFAULT , default=1) 
#     # Books = models.
#     pass

class Customer(models.Model):
    CustomerName = models.CharField(max_length=100)
    CustomerEmail = models.EmailField(max_length=100, default='abc@gmail.com')
    CustomerPassword = models.CharField(max_length=100)
    CustomerAddress = models.CharField(max_length=250 , default='Berkly street')
    CustomerAddress2 = models.CharField(max_length=250 , default='No Other Optional Address')
    CustomerPinCode =models.IntegerField(default='360005')
    BillingFirstName =models.CharField(max_length=100 , default='No Billing First Name ')
    BillingLastName = models.CharField(max_length=100 , default='No Billing Last Name ')
    CustomerState = models.CharField(max_length=100 , default='Gujarat')
    CustomerCity = models.CharField(max_length=100 , default='Rajkot')


    def __str__(self):
        return self.CustomerName
 