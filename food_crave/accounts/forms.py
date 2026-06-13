from django.forms import ModelForm
from .models import User
from django import forms


class register_user(ModelForm):
    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "phone",
            "address",
            "profile_picture",
            "password",
            "role",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        self.fields["username"].help_text = None

        self.fields["role"].widget.attrs.update({"class": "form-select"})

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class": "form-control"})

        self.fields["password"].widget.attrs.update({"class": "form-control"})

        from django.forms import ModelForm


from .models import User


class EditProfile(ModelForm):

    class Meta:

        model = User

        fields = ["username", "email", "phone", "address", "profile_picture"]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:

            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["address"].widget.attrs.update({"rows": 4})

        self.fields["username"].help_text = ""
