from django.contrib import admin
from .models import DoctorProfile,ReviewRating,Level

# Register your models here.
admin.site.register(DoctorProfile)
admin.site.register(ReviewRating)
admin.site.register(Level)
