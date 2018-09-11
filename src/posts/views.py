from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.


# I am using function based view as it is same as python function

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

#Need to wrap it and map it with url to use it

def post_detail(request): #retrieve
	#instance=Post.objects.get(id=1)
	instance=get_object_or_404(Post, id=1)
	context={"title":instance.title,
	"instance":instance,}
	return render(request,"post_detail.html",context)

def post_list(request): #list items
	
	queryset=Post.objects.all()
	context={"object_list":queryset,"title":"list"}
	# if request.user.is_authenticated:
	# 	context={"title":"my user list"}
	# else:
	# 	context={"title":"List"}
	return render(request,"index.html",context)

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")

