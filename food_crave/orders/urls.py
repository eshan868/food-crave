from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('cart/',views.cart,name='cart'),
   path('checkout/',views.checkout,name='checkout'),
   path('oder-history/',views.order_history,name='oder_history'),
   
]  
      