from django.shortcuts import render
#7. when come to fuction home(), it simply return a <h1> Blog Home </h1>
posts = [
	{
		'author': 'Xiaolong',
		'title': 'Blog Post 1',
		'content':'First post content',
		'date_posted':'June 15, 2020'
	},
	{
		'author': 'Shayna',
		'title': 'Blog Post 2',
		'content':'First post content',
		'date_posted':'June 15, 2020'
	},
	{
		'author': 'Sam',
		'title': 'Blog Post 3',
		'content':'First post content',
		'date_posted':'June 15, 2020'
	}
]
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.

#load templates

