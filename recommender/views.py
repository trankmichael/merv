from django.shortcuts import render
from .models import Rating
from django.views.generic.edit import CreateView, BaseUpdateView, BaseCreateView
from tasks.models import Task
# Create your views here.
class RatingCreateUpdate(CreateView):
	model = Rating
	fields = ['score'] 

	def form_valid(self, form):
		task_pk = self.kwargs['pk']
		task = Task.objects.get(pk=task_pk)
		user = self.request.user
		form.instance.user = user
		form.instance.task = task
		form.instance.task_pk = task_pk
		return super(RatingCreateUpdate, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		Rating.objects.filter(user=self.request.user, task=self.kwargs['pk']).delete()
		self.object = None
		return super(BaseCreateView, self).post(request, *args, **kwargs)


