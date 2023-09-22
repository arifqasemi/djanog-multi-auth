from django.urls import path
from . import views
# from django.contrib.auth import views as authentication_view
from django.contrib.auth import views as authentication_view


urlpatterns = [
    path('manager_register', views.ManagerRegisterView.as_view(), name='manager_register'),
    path('customer_register', views.CustomerRegisterView.as_view(), name='customer_register'),
    path('login/', views.LoginView, name='login'),
    path('home', views.HomeView.as_view(), name='home'),
    path('logout/', authentication_view.LogoutView.as_view(), name='logout'), 

]