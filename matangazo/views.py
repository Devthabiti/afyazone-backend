from django.shortcuts import render
from .models import Ads,Phamacy
from .serializers import AdsSerializer ,PhamacySerializer
from rest_framework import generics

# Create your views here.
class ShowAds(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
show_ads = ShowAds.as_view()


class ShowPhamacy(generics.ListAPIView):
    queryset = Phamacy.objects.all()
    serializer_class = PhamacySerializer
show_phamacy = ShowPhamacy.as_view()