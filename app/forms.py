from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }
        )
    )
    email = forms.EmailField(
        # required=False,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    # address_line1 = forms.CharField(
    #     required=False,
    #     max_length=100,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    state = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    pincode = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'city', 'state', 'pincode', 'is_admin', 'is_employee', 'is_customer')
