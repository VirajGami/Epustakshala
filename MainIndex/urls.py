from django.urls import path, include
from MainIndex.views import *

app_name = 'MainIndex'

urlpatterns = [
    path('Home/',views.index, name="index"),
    path('contact/', views.contact , name="contact"),
    path('Category/<int:id>', views.CategoryView , name="CategoryView"),
    path('Publication/<int:id>', views.PublicationView , name="PublicationView"),
    path('Author/<int:id>', views.AuthorView , name="AuthorView"),
    path('Search/', views.SearchView , name="SearchView"),
    path('Home/Details/<int:id>', views.DetailsView , name="DetailsView"),
    path('Home/Contact',views.contact,name="contact"),
    path('Home/About' , views.About , name="About"),
    path('Home/gameofthrones', views.got , name="got"),
    path('Home/HarryPotter' , views.hp , name="hp"),
    path('Home/Twilight' , views.tw , name="tw"),
    path('Home/AllBooks' , views.allBooks , name="allBooks"),
    

]