from django.urls import path, include
from MainIndex.views import *

app_name = 'MainIndex'

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/', views.contact , name="contact"),
    path('Category/<int:id>', views.CategoryView , name="CategoryView"),
    path('Publication/<int:id>', views.PublicationView , name="PublicationView"),
    path('Author/<int:id>', views.AuthorView , name="AuthorView"),
    path('Search/', views.SearchView , name="SearchView"),
    path('Details/<int:id>', views.DetailsView , name="DetailsView"),
    path('Contact',views.contact,name="contact"),
    path('About' , views.About , name="About"),
    path('gameofthrones', views.got , name="got"),
    path('HarryPotter' , views.hp , name="hp"),
    path('Twilight' , views.tw , name="tw"),
    path('AllBooks' , views.allBooks , name="allBooks"),
    

]