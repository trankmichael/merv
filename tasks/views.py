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


class TaskCreate(CreateView):
	model = Task
	template_name = 'create.html'
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

	
	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(TaskCreate, self).form_valid(form)


class TaskDetail(DetailView):
	model = Task
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

class TaskUpdate(UpdateView):
	model = Task
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def task_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 

class TaskUpdate(UpdateView):
	model = Task
	fields = ['task_name', 'collaborative','strength','transportation','outdoor','language'] 
