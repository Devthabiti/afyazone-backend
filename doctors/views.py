from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.db.models import Avg

class DoctorProfiles(APIView):
    def get(self, request, format=None):
        instance = DoctorProfile.objects.filter(isComplete=True)
        profile = DoctorProfileSerializer(instance,many=True).data

        # Function to calculate average rating
        def calculate_average_rating(reviews):
            if not reviews:
                return 0.0
            total_rating = sum(review['rating'] for review in reviews)
            return total_rating / len(reviews)
        # Sorting function
        profile.sort(key=lambda doc: (
            len(doc['review']) * calculate_average_rating(doc['review'])                            
        ), reverse=True)
        return Response(profile)
doctor_profile = DoctorProfiles.as_view()


class SendReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
send_review = SendReview.as_view()


class UpdateDoctorProfile(APIView):
    def patch(self, request, format=None):
        user_id= request.data.get('user_id')
        user = User.objects.get(id=user_id)
        profile = DoctorProfile.objects.get(user=user)
        serializer = DoctorProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
update_doctor_profile = UpdateDoctorProfile.as_view()