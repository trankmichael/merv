from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required(login_url="accounts/login")
def user_home(request):
	return render(request, "user_home.html")


def home(request):
	return render(request, "home.html")

# Http Error 400
def handler404(request):
	response = render('error404.html',{}, context_instance = RequestContext(request))
	response.status_code = 404
	return response

def handler500(request):
	response = render('error500.html', {}, context_instance = RequestContext(request))
	response.status_code = 500
	return response