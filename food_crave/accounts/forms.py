from django.forms import ModelForm
from . models import User

class register_user(ModelForm):
    class Meta:

        model=User

        fields=[
            'username',
            'email',
            'phone',
            'address',   
            'profile_picture',
            'password',
            
        ] 
class login(ModelForm):
    class Meta:
  
        model=User

        fields=[
            'username',
            'password',
        ]

