from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)  
    gender = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, default="Doctor")
    isComplete = models.BooleanField(default=False)
    region =models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    hospital = models.CharField(max_length=255, blank=True, null=True) 
    specialize = models.CharField(max_length=255, blank=True, null=True)
    price= models.IntegerField(default=5000)
    experience= models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    start_day= models.CharField(max_length=255, blank=True, null=True) 
    end_day =models.CharField(max_length=255, blank=True, null=True)   
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return f"Dr {self.first_name}  {self.last_name}" if self.first_name else self.user.username


    
class ReviewRating(models.Model):
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctor')
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='client')
    review = models.TextField()
    rating = models.FloatField()
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']