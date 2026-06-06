from django.db import models
from django.conf import settings
from restaurants.models import food_items, Restaurant
# Create your models here.

class Cart(models.Model):
    customer=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role':'customer'}

    )
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer.username
    
class cart_items(models.Model):

    cart=models.ForeignKey(
        Cart,
        on_delete=models.CASCADE

    )

    food_item = models.ForeignKey(
        food_items,
        on_delete=models.CASCADE
    )

    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.food_item.food_name


class Order(models.Model):

    STATUS_CHOICES = (
        ('placed', 'Placed'),
        ('accepted', 'Accepted'),
        ('picked', 'Picked'),
        ('delivered', 'Delivered'),
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'customer'}
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    delivery_partner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='deliveries'
    )

    delivery_otp = models.CharField(
        max_length=6,
        blank=True
    )

    is_paid = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='placed'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"oder id {self.id}"
    
class oder_items(models.Model):
    oder=models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    food_item=models.ForeignKey(
        food_items,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return self.food_item.name

