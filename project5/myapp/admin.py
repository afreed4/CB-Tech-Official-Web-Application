from django.contrib import admin
from . models import Profile_DB,Comment_DB,Blogpost_DB
# Register your models here.
admin.site.register(Profile_DB)
admin.site.register(Comment_DB)
admin.site.register(Blogpost_DB)