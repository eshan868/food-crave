from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('restaurant-dashboard/',views.restaurant_dashboard,name='restaurant-dashboard'),
   path('add-food-item/',views.add_food,name='add-food-item')
]  
