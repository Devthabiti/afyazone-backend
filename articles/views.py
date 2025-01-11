from rest_framework import generics
from .serializers import PostSerializer,CommentSerializer,LikeSerializer
from .models import Post,Like,Comment
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateArticle(generics.CreateAPIView):
    serializer_class = PostSerializer
create_article = CreateArticle.as_view()

class ShowArticle(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
show_article = ShowArticle.as_view()


class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
create_comments = CreateComment.as_view()


class LikesView(APIView):
    def post(self, request, format=None):
        post_id= request.data.get('post_id')
        client_id= request.data.get('client_id')

        post = Post.objects.get(id=post_id)
        user =User.objects.get(id=client_id)
        current_likes = post.likes
        liked = Like.objects.filter(client = user, post=post).count()
        if not liked:
            liked = Like.objects.create(client =user, post=post)
            current_likes =current_likes + 1
          
        else :
            
            liked = Like.objects.filter(client =user, post=post).delete()
            current_likes = current_likes - 1
           
        post.likes = current_likes
        post.save()

   
        return Response('success')
likes_view = LikesView.as_view()


class CountViews(APIView):
    def post(self, request, format=None):
         post_id= request.data.get('post_id')
         post = Post.objects.get(id=post_id)
         post.views = post.views  + 1
          
         if post :
            post.save()

         return Response('success')
count_view = CountViews.as_view()