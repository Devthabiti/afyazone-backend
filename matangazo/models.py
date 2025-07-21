from django.db import models

# Create your models here.
class Ads(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="ads/")

    class Meta:
        verbose_name_plural = "Ads"


class Phamacy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="dawa/")
    promo_text= models.CharField(max_length=50 ,default='Available Soon')

    class Meta:
        verbose_name_plural = "Phamacy Image"