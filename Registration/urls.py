from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'Registration'

urlpatterns = [
    # url(r'^login/$', auth_views.login, {'template_name': 'mysite/login_user.html'})
   path('Home/Login', views.Login , name='Login'),
    path('Home/Register', views.Register , name='Register'),
    path('Home/LoggedIn',views.cust_login1,name="cust_login1"),
    path('Home/LoggedOut', views.Logout, name="Logout"),
]