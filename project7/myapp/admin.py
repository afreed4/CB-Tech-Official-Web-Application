from django.contrib import admin
from . models import CustomUser,Courses,RepeatedUser,Enquery
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Courses)
admin.site.register(RepeatedUser)
admin.site.register(Enquery)
