from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm 
from django import forms


class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=30, label=_("First name"))
    last_name = forms.CharField(max_length=30, label=_("Last name"))
    collaborative = forms.CharField(max_length=30, label=_("Collaborative"))
    strength = forms.CharField(max_length=30, label=_("strength"))
    transportation = forms.CharField(max_length=30, label=_("transportation"))
    outdoor = forms.CharField(max_length=30, label=_("outdoor"))
    language = forms.CharField(max_length=30, label=_("language"))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", 'collaborative','strength','transportation','outdoor','language')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
