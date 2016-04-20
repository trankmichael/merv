"""merv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from log.forms import LoginForm
from accounts.forms import UserRegistrationForm, LoginForm
from accounts.views import UserRegistrationView
# from log.views import signup
from registration.views import RegistrationView
from . import views
from django.conf.urls import (handler400, handler403, handler404, handler500)
from rest_framework import routers, serializers, viewsets

admin.autodiscover()


handler400 = '.views.bad_request'
handler403 = '.views.permission_denied'
handler404 = '.views.page_not_found'
handler500 = '.views.server_error'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user_home/$', views.user_home, name='user_home'),
    url(r'^admin/', admin.site.urls),
	#url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),  
    url(r'^accounts/',include('accounts.urls'), name='accounts'),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    # url(r'^accounts/register/$', Re, {'template_name': 'register.html'}, name='registration_register'),
    # url(r'^accounts/login/$', views.login, {'template_name': 'login.html'}, name='registration_login'),]
]