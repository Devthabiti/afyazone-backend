from django.db import models

# Create your models here.
class Ads(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="ads/")

    class Meta:
        verbose_name_plural = "Ads"
