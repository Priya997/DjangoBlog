from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from posts import views as post_view
from . import views
urlpatterns = [

#The order of url does matter as if we have
#two url's with same name it going to stop on the 
#upper one.

	url('^$', post_view.post_list),
    url('^create/$', post_view.post_create),
    url('^detail/$', post_view.post_detail),
    url('^update/$', post_view.post_update),
    url('^delete/$', post_view.post_delete),

    #If using path('',<>) don't use ^$


    # This method is depreceated after django 1.9 don't use it 
    #url('posts/',"posts.views.post_home")

]
