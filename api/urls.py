from django.conf.urls import url, include
# from .views import TaskCreate, TaskUpdate
from tasks import views

urlpatterns = [
    url(r'^tasklist/$', views.task_list, name='task list'),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', views.task_detail, name='task detail'),
]