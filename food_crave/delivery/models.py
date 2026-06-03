from django.db import models
from django.conf import settings
# Create your models here.

class delivery_man(models.Model):
    user=models.OneToOneField(
         settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role':'delivery'}
    )

    is_available=models.BooleanField(default=False)
    
    current_latitude = models.FloatField(
        null=True,
        blank=True
    )

    current_longitude = models.FloatField(
        null=True,
        blank=True
    )
    last_location_update = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.username