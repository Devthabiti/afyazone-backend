from rest_framework import generics
from .serializers import PostSerializer,CommentSerializer,LikeSerializer
from .models import Post,Like,Comment
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Count



class CustomPagination(LimitOffsetPagination):
    default_limit = 10  # Number of records per request
    max_limit = 1000  # Maximum limit allowed in a request

class CreateArticle(generics.CreateAPIView):
    serializer_class = PostSerializer
create_article = CreateArticle.as_view()

class ShowArticle(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
show_article = ShowArticle.as_view()

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
show_article_details = ArticleDetailView.as_view()

class MostViewdArticle(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-views')[:10]  # Get only top 10 products
    serializer_class = PostSerializer
most_viewed = MostViewdArticle.as_view()


class RandomArticle(generics.ListAPIView):
    queryset = Post.objects.all().order_by('?')[:3] 
    serializer_class = PostSerializer
random_article = RandomArticle.as_view()


class MostLikedArticle(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-likes')[:10]
    serializer_class = PostSerializer
most_liked = MostLikedArticle.as_view()


class HotArticle(generics.ListAPIView):
    queryset = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:5]
    serializer_class = PostSerializer
hot_articles = HotArticle.as_view()


class ShowMagonjwa(generics.ListAPIView):
    queryset = Post.objects.filter(category="articles", label="magonjwa")[:10]
    serializer_class = PostSerializer
show_magonjwa = ShowMagonjwa.as_view()


class ShowFood(generics.ListAPIView):
    queryset = Post.objects.filter(category="articles", label="chakula")[:10]
    serializer_class = PostSerializer
food_fruit = ShowFood.as_view()


class storyTime(generics.ListAPIView):
    queryset = Post.objects.filter(category="story")
    serializer_class = PostSerializer
    pagination_class = CustomPagination
story_time = storyTime.as_view()


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