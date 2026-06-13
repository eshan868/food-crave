from django.contrib import admin
from restaurants.models import Restaurant, food_items

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(food_items)
