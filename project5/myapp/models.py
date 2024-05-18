from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.

class Profile_DB(models.Model):
    user=models.OneToOneField(User,models.CASCADE ,blank=True ,null=True)
    profile_img=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    bio=models.TextField(max_length=1000)
    phone=models.CharField(max_length=18)
    instagram=models.CharField(max_length=280, blank=True)
    linkdin=models.CharField(max_length=180, blank=True)
    facebook=models.CharField(max_length=200, blank=True)   
    
    def __str__(self):
        return str(self.user)
    
class Blogpost_DB(models.Model):
    title=models.CharField(max_length=190)
    author=models.ForeignKey(User, on_delete=models.CASCADE,)
    slug=models.CharField(max_length=290)
    content=models.TextField()
    blog_img=models.ImageField(upload_to='blog_post')
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) + 'Blog Title:' + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
class Comment_DB(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    blog=models.ForeignKey(Blogpost_DB, on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dateTime=models.DateTimeField(default=now)
    
    def __str__(self):
        return self.user.username + "Comment:" + self.content
