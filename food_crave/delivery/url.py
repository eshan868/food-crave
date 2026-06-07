from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('delivery-dashboard/',views.delivery_dashboard,name='delivery-man-dashboard'),
   path('new-orders/',views.new_orders,name='new-delivery'),
   path('accept-order/<int:order_id>/', views.accept_order,name='accept_order'),
   path('picked-order/<int:order_id>/',views.picked_order, name='picked_order'),
   path('verify-otp/<int:order_id>/',views.verify_otp,name='verify_otp'),
   path('update-location/',views.update_location,name='update_location'),


]
