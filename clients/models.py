from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClientProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=255,unique=True, blank=True, null=True) 
    gender = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, default="Client")
    isComplete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="client/", blank=True, null=True)

    def __str__(self): 
        return self.username if self.username else self.user.username


class Transactions(models.Model):
    choice = (
        ('paid','PAID'),
        ('Not','NOT PAID'), 
      )
    client = models.ForeignKey(User, on_delete=models.CASCADE,related_name='mgongwa')
    doctor = models.ForeignKey(User,  on_delete=models.CASCADE,related_name='daktari')
    payment_phone = models.CharField(max_length=15,)
    order_id = models.CharField(max_length=255,)
    amount= models.CharField(max_length=15,)
    status= models.CharField(max_length=20 ,choices=choice, default='Not')
