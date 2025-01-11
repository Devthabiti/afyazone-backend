# urls.py
from django.urls import path
from .views import *
from clients.views import *
from doctors.views import *
from message.views import *
from articles.views import *
from matangazo.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
  
)


urlpatterns = [
    #login and user authentications
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('send-otp/',send_sms, name='send-otp'),
    path('login/',creates_user, name='login'),
    path('details/',user_details, name='details'),
    
   # clients urls
   path('update-profile/',update_profile, name='update-profile'),
   path('create-transaction/',create_transaction, name='create-transaction'),
   path('show-transaction/',show_transaction, name='show-transaction'),
   path('view-client-profile/',client_profile, name='view-client-profile'),

    # doctors urls
    path('doctors/',doctor_profile, name='doctors'),
    path('send-review/',send_review, name='send-review'),
    path('update-doctor-profile/',update_doctor_profile, name='update-doctor-profile'),


    # Chat/Text Messaging Functionality
    path("my-messages/<user_id>/", MyInbox.as_view()),
    path("get-messages/<sender_id>/<reciever_id>/", GetMessages.as_view()),
    path("send-messages/", SendMessages.as_view()),


    # articles and story urls
    path('post-article/',create_article, name='post-article'),
    path('show-article/',show_article, name='show-article'),
    path('create-comments/',create_comments, name='create-comments'),
    path('likes/',likes_view, name='likes'),
    path('views/',count_view, name='views'),


    # advatizement
    path('ads/',show_ads, name='ads'),
 
]
