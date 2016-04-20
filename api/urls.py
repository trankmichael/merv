from django.conf.urls import url, include
# from .views import TaskCreate, TaskUpdate
from tasks import views as task_views
from accounts import views as account_views

urlpatterns = [
    url(r'^tasklist/$', task_views.TaskList.as_view(), name='task list'),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', task_views.TaskDetail.as_view(), name='task detail'),
    url(r'^userlist/$', account_views.UserList.as_view()),
    url(r'^userdetail/(?P<pk>[0-9]+)/$', account_views.UserDetail.as_view()),
]