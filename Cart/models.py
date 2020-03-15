from django.db import models
from Registration.models import Customer
from MainIndex.models import Book





# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=15)
    item = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f'{self.quantity} of {self.item.BookName }'

    def get_total(self):
        total = self.item.BookPrice * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal

    def cart_delete(self):
        self.delete()
    
    

# Order Model
class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE , default=12)
    # alreadyregistered = models.IntegerField(default=0)
    def __str__(self):
        return self.user.CustomerName
    
    def get_totals(self):
        total =0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
        return total