from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from  imagekit.processors import ResizeToFill
import uuid

# Create your models here.

class Albums(models.Model):
    title=models.CharField(max_length=790);
    thump=ProcessedImageField(upload_to='images/',processors=[ResizeToFill(300)], format='JPG',options={'quality':80})
    visible=models.BooleanField(default=True)
    discription=models.TextField(max_length=1039)
    create=models.DateTimeField(auto_now_add=True)
    modify=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True,max_length=250,blank=False)
    
    def __unicode__(self):
        return self.title
    
class AlbumDetailView(models.Model):
    image=ProcessedImageField(upload_to='images/',processors=[ResizeToFill(1280)],format='JPG',options={'quality':70})
    thump=ProcessedImageField(upload_to='images/',processors=[ResizeToFill()],format='JPG',options={'quality':80})
    album=models.ForeignKey('Albums',on_delete=models.PROTECT)
    alt=models.CharField(max_length=1200,default=uuid.uuid4)
    created=models.DateField(auto_now_add=True)
    width=models.IntegerField(default='0')
    height=models.IntegerField(default='0')
    slug=models.SlugField(max_length=100, default=uuid.uuid4, editable=False )
    


