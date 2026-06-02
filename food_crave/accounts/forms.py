from django.forms import ModelForm
from . models import User
from django import forms
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
            'role',  
             
        ] 
class Login(forms.Form):
    username = forms.CharField()   
    password=forms.CharField(
        widget=forms.PasswordInput()
    )