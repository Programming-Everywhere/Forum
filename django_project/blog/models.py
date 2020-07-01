from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 100) #The char length
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)#Only when object created

	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
