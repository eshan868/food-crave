from django.db import models
from django.conf import settings

# Create your models here.


class Restaurant(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "restuarant_owner"},
    )

    shop_name = models.CharField(max_length=100)
    address = models.TextField()
    restaurant_image = models.ImageField(upload_to="media/restaurant_images/")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.shop_name


class food_items(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    food_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    food_image = models.ImageField(
        upload_to="media/food_images/", null=True, blank=True
    )

    def __str__(self):
        return self.food_name, self.price
