from django.urls import path
from . import views
# 4.after came here, the page will look after blog/, 
# 5.since it is empty, then let's look if there is empty in the pattern
# 6.yes, there is. then where the empty take us. to the view.py fuction home()
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]