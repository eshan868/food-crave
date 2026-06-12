from django.forms import ModelForm
from .models import food_items
from .models import Restaurant


class food_items_form(ModelForm):

    class Meta:

        model = food_items

        fields = [
            'restaurant',
            'food_name',
            'description',
            'price',
            'food_image',
            
        ]
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class Restaurant_form(ModelForm):
    class Meta:
        model = Restaurant

        fields = [
            'shop_name',
            'address',
            'restaurant_image'
        ]
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                'class': 'form-control'
            })