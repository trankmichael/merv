from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile
from registration import signals

from .forms import UserRegistrationForm
from .models import User
from rest_framework import generics
from accounts.serializers import UserSerializer


class UserRegistrationView(RegistrationView):
    form_class = UserRegistrationForm

    # def get_success_url(self, request, user):
    #     return "/user_home"

    def register(self, form):
        request = self.request
        site = get_current_site(request)

        if hasattr(form, 'save'):
            new_user_instance = form.save()
        else:
            new_user_instance = (User().objects
                                 .create_user(**form.cleaned_data))

        new_user = RegistrationProfile.objects.create_inactive_user(
            new_user=new_user_instance,
            site=site,
            send_email=self.SEND_ACTIVATION_EMAIL,
            request=request,
        )
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer