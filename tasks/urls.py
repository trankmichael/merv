from django.conf.urls import url, include
from .views import TaskCreate, TaskUpdate
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^create/$', TaskCreate.as_view(), name='task-add'),
    url(r'^(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-detail'),

<<<<<<< HEAD
    # url(r'^tasklist/$', views.task_list),
    # url(r'^taskdetail/(?P<pk>[0-9]+)/$', views.task_detail),
]
=======
    url(r'^tasklist/$', views.TaskList.as_view()),
    url(r'^taskdetail/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> 043ef0f91be9cf76989b513660f51bd2912e1c2c
