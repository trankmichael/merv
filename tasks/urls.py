from django.conf.urls import url, include
from .views import TaskCreate, TaskUpdate, TaskList, TaskDetail
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^create/$', TaskCreate.as_view(), name='task-add'),
    url(r'^(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-detail'),
    # url(r'^tasklist/$', views.task_list),
    url(r'^tasklist/$', TaskList.as_view()),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', TaskDetail.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)
