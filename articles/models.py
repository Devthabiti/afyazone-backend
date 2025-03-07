from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    choice = (
        ('articles','ARTICLES'),
        ('story','STORY'), 
      )
    choice2 = (
        ('magonjwa','MAGONGWA'),
        ('chakula','CHAKULA'), 
        ('others','OTHERS'), 
      )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=100, editable=False)
    likes = models.PositiveIntegerField(default=55, editable=False)
    image = models.ImageField(upload_to="articles/",)
    category= models.CharField(max_length=20 ,choices=choice)
    label= models.CharField(max_length=20 ,choices=choice2, default='others')


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title}' 

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.client.username}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='postlikes', on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    
   

    def __str__(self):
        return f'Like by {self.client.username}'
