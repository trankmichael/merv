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
from scipy import spatial
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from recommender.models import CosineTaskSimilarity
from operator import itemgetter




class TaskCreate(CreateView):
    model = Task
    template_name = 'create.html'
    fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

    
    def form_valid(self, form):
        print('hello')
        user = self.request.user
        form.instance.user = user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        import cProfile, pstats, StringIO
        pr = cProfile.Profile()
        pr.enable()
        tasks = Task.objects.all()
        user = self.request.user
        task_list = []
        returned_list = []
        user_vector = [user.collaborative, user.strength, user.transportation, user.outdoor, user.language]
        for obj in tasks[:20]:
            task_vector = [obj.collaborative, obj.strength, obj.transportation, obj.outdoor, obj.language]
            score = 1 - spatial.distance.cosine(task_vector, user_vector)
            task_list.append((obj, score))
            cosine_similarity = CosineTaskSimilarity(user=user, task=obj.pk, similarity=score)
            cosine_similarity.save()
        task_list.sort(key=itemgetter(1), reverse = True)
        for item in task_list:
            returned_list.append(item[0])
        serializer = TaskSerializer(returned_list, many=True)

        pr.disable()
        s = StringIO.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def generate(request):
    data = []
    for i in range(0,1000):
        data.append(i)
        data.append('a')
        for j in range(0,5):
            x = random.randint(1, 100)
            if x <= 5:
                data.append('0')
            elif x > 5 and x <= 10:
                data.append('1')
            elif x > 10 and x <= 15:
                data.append('2')
            elif x > 20 and x <= 25:
                data.append('3')
            elif x > 25 and x <= 30:
                data.append('4')
            else:
                data.append('5')
        task = Task(
            id=data[0],
            task_name=data[1],
            collaborative=data[2],
            strength=data[3],
            transportation=data[4],
            outdoor=data[5],
            language=data[6])
        task.save()
        del data[:]
    return ('uploaded')