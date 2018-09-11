from django.contrib import admin
from .models import Post 
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	# to show the multiple things in admin panel
	list_display=["title","updated","timestamp"]
	# to show the link on updated
	list_display_links=["updated"]
	# To edit the title in the admin panel
	list_editable=['title']
	# to add filter
	list_filter=["updated","timestamp"]
	# to add search on admin panel
	search_fields=['title','content']	 
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)