from django.conf.urls import url, include
# from .views import TaskCreate, TaskUpdate
from tasks import views

urlpatterns = [
    url(r'^tasklist/$', views.TaskList.as_view(), name='task list'),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task detail'),
]