from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('restaurant_owner', 'Restaurant_owner'),   
        ('delivery_man', 'Delivery_man'),
    )

    role=models.CharField(
        max_length=100,
        choices=ROLE_CHOICES
    )

    phone=models.CharField(max_length=15)
    address=models.TextField()
    profile_picture = models.ImageField(
        upload_to='media/profile_pictures/',
        blank=True,
        null=True
    )
    latitude = models.FloatField(
        
        null=True,
        blank=True

    )

    longitude = models.FloatField(

        null=True,
        blank=True
    )
    def __str__(self):
        return self.username
    
