from django.shortcuts import render
from .models import Rating
from django.views.generic.edit import CreateView
# Create your views here.
class RatingCreate(CreateView):
	model = Rating
	template_name = 'create.html'
	fields = ['score'] 

	
	def form_valid(self, form):
		print('hello')
		task = Task.objects.get(pk=kwargs['pk'])
		user = self.request.user
		form.instance.user = user
		form.instance.task = task
		return super(TaskCreate, self).form_valid(form)
