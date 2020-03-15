from django.db import models
# Create your models here.
class Category(models.Model):
  CategoryName = models.CharField(max_length=80)
  CategoryImage =models.CharField(max_length=250)

  def __str__(self):
    return self.CategoryName

  def get_products(self):
    return Book.objects.filter(Category__CategoryName=self.CategoryName)


class Publication(models.Model):
  PublicationImage = models.CharField(max_length=250)
  PublicationName = models.CharField(max_length=80)
  PublicationDesc = models.CharField(max_length=250)

  def __str__ (self):
    return self.PublicationName

class Author(models.Model):
    AuthorImage = models.CharField(max_length=250, default="http://quoteslab.net/contents/uploads/bill-cameron-mystery-author-400x400.jpg")
    AuthorName = models.CharField(max_length=80)
    AuthorEmail = models.EmailField()
    AuthorDesc = models.CharField(max_length=250)

    def __str__(self):
      return self.AuthorName
    

class Book(models.Model):
    BookImage=models.CharField(max_length=5000, default="http://www.macedonrangeshalls.com.au/wp-content/uploads/2017/10/image-not-found.png")
    BookName= models.CharField(max_length=50)
    BookDesc=models.CharField(max_length=500)
    Author=models.ForeignKey( Author, on_delete=models.SET_DEFAULT, default=1)
    Publication= models.ForeignKey( Publication , on_delete=models.SET_DEFAULT , default=1)
    Category = models.ForeignKey( Category , on_delete=models.SET_DEFAULT  , default=1)
    BookPrice=models.IntegerField()
    BookStock=models.IntegerField()
    SubCategory = models.CharField(max_length=150, default="NULL")

    def __str__(self):
      return self.BookName

class Contact(models.Model):
  FullName = models.CharField(max_length=250)
  Email = models.EmailField()
  Phone = models.IntegerField()
  Message = models.CharField(max_length=550)

  def __str__(self):
    return self.FullName