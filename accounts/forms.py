from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm 
from django import forms


class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=30, label=_("First name"))
    last_name = forms.CharField(max_length=30, label=_("Last name"))
    attribute_1 = forms.CharField(max_length=30, label=_("Attribute 1"))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "attribute_1")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
