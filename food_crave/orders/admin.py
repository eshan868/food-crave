from django.contrib import admin

# Register your models here.
from accounts.models import User
from restaurants.models import Restaurant, food_items
from orders.models import Order
from delivery.models import DeliveryAssignment


admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(food_items)
admin.site.register(Order)
admin.site.register(DeliveryAssignment)