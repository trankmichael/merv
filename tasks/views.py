from django.shortcuts import render
from .models import Task
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Task 

class TaskCreate(CreateView):
	model = Task
	template_name = 'create.html'
	fields = ['collaborative','strength','transportation','outdoor','language'] 
	
	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(TaskCreate, self).form_valid(form)


class TaskDetail(DetailView):
	model = Task
	fields = ['collaborative','strength','transportation','outdoor','language'] 

class TaskUpdate(UpdateView):
	model = Task
	fields = ['collaborative','strength','transportation','outdoor','language'] 
