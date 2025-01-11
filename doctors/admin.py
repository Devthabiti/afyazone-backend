from django.contrib import admin
from .models import DoctorProfile,ReviewRating

# Register your models here.
admin.site.register(DoctorProfile)
admin.site.register(ReviewRating)
