from django.conf.urls import url, include
from .views import UserRegistrationView
# from registration.views import RegistrationView
from .forms import UserRegistrationForm    
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^register/$', UserRegistrationView.as_view(form_class=UserRegistrationForm),
        name='registration_register',),
    url(r'^', include('registration.backends.default.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)