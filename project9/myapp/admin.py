from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from .models import customuser, AdminHOD, Staffs, Students, Attendance, AttendanceReport
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(customuser)
admin.site.register(AdminHOD)
admin.site.register(Attendance)
admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(AttendanceReport)
