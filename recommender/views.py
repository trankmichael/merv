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
            newratings = RecommenderFile(ratings_csv = request.FILES['ratings_csv'])
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

# class CollaborativeList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         tasks = Task.objects.all()
#         user = self.request.user
#         task_list = []
#         returned_list = []
#         user_vector = [user.collaborative, user.strength, user.transportation, user.outdoor, user.language]
#         for obj in tasks:
#             task_vector = [obj.collaborative, obj.strength, obj.transportation, obj.outdoor, obj.language]
#             score = 1 - spatial.distance.cosine(task_vector, user_vector)
#             task_list.append((obj, score))
#             cosine_similarity = CosineTaskSimilarity(user=user, task=obj.pk, similarity=score)
#             cosine_similarity.save()
#         task_list.sort(key=itemgetter(1), reverse = True)
#         for item in task_list:
#             returned_list.append(item[0])
#         serializer = TaskSerializer(returned_list, many=True)

#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
