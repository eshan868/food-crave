from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('register/',views.register,name='registre'),
   path('login/',views.login,name='login'),
   path('user-dashboard/',views.customer_dashboard,name='customer-dashboard')
   
]
