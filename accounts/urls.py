from django.conf.urls import url, include
from .views import UserRegistrationView

from .forms import UserRegistrationForm    

urlpatterns = [
    url(r'^register/$', RegistrationView.as_view(form_class=UserRegistrationForm),
        name='registration_register',),
    url(r'^', include('registration.backends.default.urls')),
]