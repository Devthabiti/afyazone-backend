from .models import ChatMessage,User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db.models import OuterRef, Subquery
from django.db.models import Q
from clients.serializers import ClientProfileSerializer
from doctors.serializers import DoctorProfileSerializer


class MessageSerializer(serializers.ModelSerializer):   
    sender_profile = ClientProfileSerializer(read_only=True)
    reciever_profile = DoctorProfileSerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = '__all__'
        #fields = ['id','message', 'is_read', 'date','sender', 'reciever',  'sender_profile','reciever_profile', ]
    
    # def __init__(self, *args, **kwargs):
    #     super(MessageSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method=='POST':
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 2

    # def get_idadi(self,data):
    #     request = self.context.get('request')
    #     user_id = request.data['user_id']
  
    #     #user_id = self.kwargs['user_id']
    #     number= ChatMessage.objects.filter(
    #         id__in =  Subquery(
    #             User.objects.filter(
    #                 Q(sender__reciever=user_id) |
    #                 Q(reciever__sender=user_id)
    #             ).distinct().annotate(
    #                 last_msg=Subquery(
    #                     ChatMessage.objects.filter(
    #                         Q(sender=OuterRef('id'),reciever=user_id) |
    #                         Q(reciever=OuterRef('id'),sender=user_id)
    #                     ).order_by('-id')[:1].values_list('id',flat=True) 
    #                 )
    #             ).values_list('last_msg', ).order_by("-id")
    #         )
    #     ).filter(is_read = False).count()
    #    # print(number)
    #     return number

