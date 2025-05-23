# serializers.py
from rest_framework import serializers
from .models import DoctorProfile,ReviewRating
from django.contrib.auth.models import User
from clients.models import ClientProfile,Transactions
from clients.serializers import ClientProfileSerializer,TransactionSerializer


class ReviewSerializer(serializers.ModelSerializer):
    client_profile = serializers.SerializerMethodField()
    class Meta:
        model= ReviewRating
        #fields =['id','name','age','color','mtoto','babu']
        fields= '__all__'
    def get_client_profile(self, data):
            prof = ClientProfile.objects.get(user=data.client)
            profile = ClientProfileSerializer(prof).data
            return profile



class DoctorProfileSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    patient =serializers.SerializerMethodField()
    class Meta:
        model = DoctorProfile
        fields = '__all__'
      

    def get_review(self, data):
            user = User.objects.get(id=data.user.id)
            
            instance = ReviewRating.objects.filter(doctor=user)
            profile = ReviewSerializer(instance,many=True).data
            return profile
            # if data.age > 30:
            #     return {"isMzee":True,"age":data.age,"fav_color":cl.color_name}
            # else:
            #     return 'Bado mtoto mdgo'

    def get_patient(self, data):
            user = User.objects.get(id=data.user.id)
            
            instance = Transactions.objects.filter(doctor=user)
            profile = TransactionSerializer(instance,many=True).data
            return profile
            # if data.age > 30:
            #     return {"isMzee":True,"age":data.age,"fav_color":cl.color_name}
            # else:
            #     return 'Bado mtoto mdgo'




      