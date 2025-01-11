from rest_framework import serializers
from .models import Post, Comment, Like
from clients.models import ClientProfile
from clients.serializers import ClientProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    client_profile = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_client_profile(self, data):
            prof = ClientProfile.objects.get(user=data.client)
            profile = ClientProfileSerializer(prof).data
            return profile

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        #fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    postlikes = LikeSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
