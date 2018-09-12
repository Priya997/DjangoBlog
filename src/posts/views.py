from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

from .form import PostForm
# I am using function based view as it is same as python function


def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
	# if request.method=="POST":
	# 	print(request.POST.get("content"))
	# 	print(request.POST.get("title"))
	context={"form":form,}
	return render(request,"post_form.html",context)



#Need to wrap it and map it with url to use it

def post_detail(request, id=None): #retrieve
	#instance=Post.objects.get(id=1)
	instance=get_object_or_404(Post, id=id)
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

