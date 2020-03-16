from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'Registration'

urlpatterns = [
    # url(r'^login/$', auth_views.login, {'template_name': 'mysite/login_user.html'})
   path('Login', views.Login , name='Login'),
    path('Register', views.Register , name='Register'),
    path('LoggedIn',views.cust_login1,name="cust_login1"),
    path('LoggedOut', views.Logout, name="Logout"),
]