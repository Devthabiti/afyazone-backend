from django.contrib import admin
from .models import  ChatMessage

# class ProfileAdmin(admin.ModelAdmin):
#     list_editable = ['verified']
#     list_display = ['user', 'full_name' ,'verified']

# class ChatMessageAdmin(admin.ModelAdmin):
#     list_editable = ['is_read', 'message']
#     list_display = ['user','sender', 'reciever', 'is_read', 'message']


# admin.site.register( Profile,ProfileAdmin)
# admin.site.register( ChatMessage,ChatMessageAdmin)

# Register your models here.
admin.site.register(ChatMessage)
