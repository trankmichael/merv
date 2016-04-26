from django.shortcuts import render, render_to_response
from .models import Rating, RecommenderFile
from django.views.generic.edit import CreateView, BaseUpdateView, BaseCreateView
from tasks.models import Task
from .algorithms.mervrecsys import generate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import RecommenderFile
from .forms import RatingUpload
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

def GenerateRecommendations(request):
	generate('/data/ratings.dat')
	return HttpResponse('<h1>Page was found</h1>')


def ratings_list(request):
    # Handle file upload
    if request.method == 'POST':
        form = RatingUpload(request.POST, request.FILES)
        if form.is_valid():
            newratings = RecommenderFile(docfile = request.FILES['docfile'])
            newratings.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('recommender.views.list'))
    else:
        form = RatingUpload() # A empty, unbound form

    # Load documents for the list page
    ratings = RecommenderFile.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'recommender/list.html',
        {'ratings': ratings, 'form': form},
        context_instance=RequestContext(request)
    )