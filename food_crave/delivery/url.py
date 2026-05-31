from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('delivery-dashboard/',views.delivery_dashboard,name='delivery-man-dashboard'),
   path('new-orders/',views.new_orders,name='new-delivery')
]
