from django.shortcuts import render
from .models import Ads
from .serializers import AdsSerializer
from rest_framework import generics

# Create your views here.
class ShowAds(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
show_ads = ShowAds.as_view()
