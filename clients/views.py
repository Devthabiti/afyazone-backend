from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from .models import ClientProfile,Transactions
from .serializers import ClientProfileSerializer,TransactionSerializer
from rest_framework.response import Response
from rest_framework import status

class UpdateProfile(APIView):
    def patch(self, request, format=None):
        user_id= request.data.get('user_id')
        user = User.objects.get(id=user_id)
        profile = ClientProfile.objects.get(user=user)
        serializer = ClientProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
update_profile = UpdateProfile.as_view()


class ClientProfiles(APIView):
    def post(self, request, format=None):
        user_id= request.data.get('user_id')
        user = User.objects.get(id=user_id)
        instance = ClientProfile.objects.get(user=user)
        profile = ClientProfileSerializer(instance).data
        return Response(profile)
client_profile = ClientProfiles.as_view()

class CreateTransaction(generics.CreateAPIView):
    serializer_class = TransactionSerializer
create_transaction = CreateTransaction.as_view()


class ShowTransaction(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
show_transaction = ShowTransaction.as_view()