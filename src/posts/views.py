from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# I am using function based view as it is same as python function

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

#Need to wrap it and map it with url to use it

def post_detail(request): #retrieve
	return HttpResponse("<h1>Detail</h1>")

def post_list(request): #list items
	return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")

