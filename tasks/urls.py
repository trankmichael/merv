from django.conf.urls import url, include
from .views import TaskCreate, TaskUpdate

urlpatterns = [
    url(r'^create/$', TaskCreate.as_view(), name='task-add'),
    url(r'^(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-detail'),
]