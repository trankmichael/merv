from django.conf.urls import url, include
from .views import TaskCreate, TaskUpdate
from tasks import views

urlpatterns = [
    url(r'^create/$', TaskCreate.as_view(), name='task-add'),
    url(r'^(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-detail'),

    url(r'^tasklist/$', views.task_list),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', views.task_detail),
]