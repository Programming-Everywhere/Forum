from django.shortcuts import render
from .models import Post
#7. when come to fuction home(), it simply return a <h1> Blog Home </h1>
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.

#load templates

