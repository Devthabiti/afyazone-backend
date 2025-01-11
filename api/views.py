from django.contrib.auth.models import User
import random
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clients.models import ClientProfile
from doctors.models import DoctorProfile
import requests




class CreateUser(APIView):
    def post(self ,request):
        phone =request.data.get('phone')

        try:
            # authenticate or create user
            user, created = User.objects.get_or_create(username=phone)
            # print('huyu user ',user)
            # print('created ',created)
            
            #create profile
            if created:
                profile = ClientProfile.objects.create(
                            user=user,
                            phone= phone
                        )
                profile.save()
            else :
                user_profile = ClientProfile.objects.filter(user=user).exists()
                # print('tuone',user_profile)

                if not user_profile:
                    #create doctor profile
                    profile = DoctorProfile.objects.get_or_create(
                            user=user,
                            phone= phone
                        )
                    #profile.save()
                    # print('heee ndo nataka mm')

            # Optionally, create or update a token for the user
           # token, createds = Token.objects.get_or_create(user=user) 
            toke = AccessToken.for_user(user)
            # print('huyu user token yake :',toke)
            #print('created ',createds)

            return Response({
                "message": "Code verified successfully",
                "token": str(toke)
            }, status=status.HTTP_200_OK)

        except :
            return Response({"error": "Invalid code or phone number"}, status=status.HTTP_400_BAD_REQUEST)

       # return Response('ERRORS OCCURED', status=status.HTTP_400_BAD_REQUEST)
creates_user = CreateUser.as_view()


class UserDetails(APIView):
    def post(self ,request):
        user_id= request.data.get('id')
        user = User.objects.get(id=user_id)
        client_profile = ClientProfile.objects.filter(user=user).first()
        if client_profile:
            return Response({"role": client_profile.role,"completed":client_profile.isComplete})
        else :
            client=  DoctorProfile.objects.filter(user=user).first()            
            return Response({"role" : client.role,"completed":client.isComplete})
user_details = UserDetails.as_view()
   


class Sendsms(APIView):
    def post(self ,request):
        otp = random.randint(100000, 999999)
        phone =request.data.get('phone')
        print(phone)
        url = 'https://messaging-service.co.tz/api/sms/v1/text/single'
        body = {
                "from": "AFYAZONE",
                "to": phone,
                 "text": f"Your AFYAZONE otp is {otp}",#"text": f"{otp} is Your Verification code for Afyazone App ", 
                "reference": f"{otp}zone"
                }
        headers = {
                    'Authorization': 'Basic bWF0aWt1OmJpcGFzMTIzNA==',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                    }
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            output = response.json()
            # print(output)
            data = output['messages'][0]['status']['groupId']
            # print(data)
            # print(type(data))
            if data == 18:
                txt =output['messages'][0]['message']
                my_otp = txt[-6:]
                # print('message imefika')
                # print(my_otp)
                return Response({"message":"Otp Send successfully","otp":my_otp,"phone_number":phone})
            else : 
                return Response("Invalid phone number or internet connections", status=status.HTTP_404_NOT_FOUND)
    
        else :
            return Response({"Error":"Request failed with status code"}, status=status.HTTP_404_NOT_FOUND)
send_sms = Sendsms.as_view()

   
