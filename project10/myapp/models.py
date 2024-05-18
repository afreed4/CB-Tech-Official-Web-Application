from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.

class Counsillors(models.Model):
    coun_user=models.OneToOneField(User,models.CASCADE,null=True,blank=False)
    name=models.CharField(max_length=200,null=True)

class Student(models.Model):
    student_registration_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=240,null=True)
    counsillor_name=models.OneToOneField(Counsillors,models.CASCADE,null=True)
    
    
class Faculty(models.Model):
    fac_user=models.OneToOneField(User,models.CASCADE,null=True,blank=True)
    name=models.OneToOneField(Student, models.CASCADE,null=True)
    #student_registration_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    #attendence_view=models.OneToOneField()
   
    
class Attendence(models.Model):
    id_of_attendence=models.AutoField(primary_key=True)
    #student_registration_id=models.ForeignKey(Student,on_delete=models.CASCADE,default=0)
    attendence_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=False)
    status=models.CharField(max_length=200,null=True)
    objects=models.Manager()
    

class AttendenceReport(models.Model):
    attendence_report_id=models.AutoField(primary_key=True)
    student_registration_id=models.ForeignKey(Student,on_delete=models.CASCADE,default=0)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=False)
    objects=models.Manager()


