from django.db import models

# Create your models here.
#mvc->Model view controller

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	# if using python 2
	def __uniode__(self):
		return self.title

	# if using python 3
	def __str__(self):
		return self.title