from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from  imagekit.processors import ResizeToFill
# Create your models here.

class Datas(models.Model):
    Name=models.CharField(max_length=250)
    Number=models.IntegerField(null=True)
    Club=models.TextField()

class Photo(models.Model):
    #image=models.ImageField(upload_to='photos/')
    image=ProcessedImageField(upload_to='photos/',processors=[ResizeToFill(width=200, height=200)], format='JPEG', options={'quality': 70})