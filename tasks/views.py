from django.shortcuts import render
from .models import Task
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Task 

class TaskCreate(CreateView):
	model = Task
	template_name = 'create.html'
	fields = ['attribute_1','attribute_2','attribute_3','attribute_4','attribute_5','attribute_6','attribute_7','attribute_8','attribute_9','attribute_10']
	
	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(TaskCreate, self).form_valid(form)



class TaskUpdate(UpdateView):
    model = Task
    fields = ['attribute_1','attribute_2','attribute_3','attribute_4','attribute_5',
		'attribute_6','attribute_7','attribute_8','attribute_9','attribute_10']
