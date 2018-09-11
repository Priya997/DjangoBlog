from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# I am using function based view as it is same as python function

def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

#Need to wrap it and map it with url to use it



