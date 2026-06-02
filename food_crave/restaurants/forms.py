from django.forms import ModelForm
from .models import food_items


class food_items_form(ModelForm):

    class Meta:

        model = food_items

        fields = [
            'food_name',
            'description',
            'price',
            'food_image',
            
        ]