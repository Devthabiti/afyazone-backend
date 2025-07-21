from rest_framework import serializers
from .models import Ads,Phamacy

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'


class PhamacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Phamacy
        fields = '__all__'