from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    email = models.CharField(max_length=90)
    sei = models.CharField(max_length=80)
    mei = models.CharField(max_length=80)
    sei_kana = models.CharField(max_length=100)
    mei_kana = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    
