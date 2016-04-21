from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.serializers import TaskSerializer

from django.shortcuts import render
from .models import Task
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from rest_framework import generics

class TaskCreate(CreateView):
	model = Task
	template_name = 'create.html'
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

	
	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
	model = Task
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer