from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from posts import views as post_view
from . import views

app_name='posts'
urlpatterns = [

#The order of url does matter as if we have
#two url's with same name it going to stop on the 
#upper one.

	url('^$', post_view.post_list),
    url('^create/$', post_view.post_create),
    url('^(?P<id>\d+)/$', post_view.post_detail,name='detail'),
    url('^(?P<id>\d+)/edit/$', post_view.post_update,name='update'),
    url('^delete/$', post_view.post_delete),

    #If using path('',<>) don't use ^$


    # This method is depreceated after django 1.9 don't use it 
    #url('posts/',"posts.views.post_home")

]
