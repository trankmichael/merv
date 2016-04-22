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

	# def get(self, request, *args, **kwargs):
	# 	queryset = Rating.objects.filter(user=self.request.user, task=self.kwargs['pk'])
	# 	if queryset.exists():
	# 		self.object = self.get_object()
	# 		return super(BaseUpdateView, self).get(request, *args, **kwargs)
	# 	else:
	# 		self.object = None
	# 		return super(BaseCreateView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		Rating.objects.filter(user=self.request.user, task=self.kwargs['pk']).delete()
		self.object = None
		return super(BaseCreateView, self).post(request, *args, **kwargs)
		# if queryset.exists():
		# 	#update rating if it already exists 
		# 	self.object = self.get_object()
		# 	return super(BaseUpdateView, self).post(request, *args, **kwargs)
		# else:
		# 	#create rating if it doesnt
		# 	self.object = None
		# 	return super(BaseCreateView, self).post(request, *args, **kwargs)

	# def get_object(self, queryset=None):
	# 	queryset = Rating.objects.filter(user=self.request.user, task=self.kwargs['pk'])
	# 	print queryset
	# 	try:
	# 		return super(RatingCreateUpdate,self).get_object(queryset)
	# 	except AttributeError:
	# 		return None

	# def get(self, request, *args, **kwargs):
	# 	self.object = self.get_object()
	# 	return super(RatingCreateUpdate, self).get(request, *args, **kwargs)

	# def post(self, request, *args, **kwargs):
	# 	self.object = self.get_object()
	# 	return super(RatingCreateUpdate, self).post(request, *args, **kwargs)

