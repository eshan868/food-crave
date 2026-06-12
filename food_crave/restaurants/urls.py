from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('restaurant-dashboard/',views.restaurant_dashboard,name='restaurant-owner-dashboard'),
   path('add-food-item/',views.add_food,name='add-food-item'),
   path('add-restaurant/',views.add_restaurant,name='add-restaurant'),
   path("restaurant/edit/<int:restaurant_id>/", views.edit_restaurant, name="edit_restaurant"),
   path("restaurant/delete/<int:restaurant_id>/", views.delete_restaurant, name="delete_restaurant"),
   path('food/edit/<int:food_id>/',views.edit_food,name='edit_food'),
   path('food/delete/<int:food_id>/',views.delete_food,name='delete_food'),
   path('restaurants/',views.all_restaurants,name='all_restaurants'),
   path('restaurant/<int:id>/',views.restaurant_detail,name='restaurant_detail'),
]  
