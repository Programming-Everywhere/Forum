0. python3 -m pip install django-crispy-forms
0. create a app: 
  ```html
    python manage.py startapp user 
  ```
1. create a user: in web
2. create a post 
   1) login python3 manage.oy shell
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()

  2) find all users: User.objects.all()
  
  3)creating varibale: user = User.objects.filter(username='Shyna') 

  4) user1 = User.objects.filter(username='xiaolong').first() 0> this will see the user infromation, ID, email ...
  5) varible post_1: post_1 = Post(title = 'Blog 4', content = 'the #4 blog', author=user1)
  6) post_1.save()
 
3.[no need to use .save()]  user.post user.post_set.create(title='Blog 5', content='#5 blog')


*** always push the code by using 
```html
push
``` 
