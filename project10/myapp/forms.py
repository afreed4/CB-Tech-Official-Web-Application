from django import forms

from . models import Student,Faculty,Counsillors,Attendence,AttendenceReport
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SighnupForm(UserCreationForm):
    class Meta:
        model=User;
        fields=['username','password1','password2']
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput) 


class StudentForm(forms.Form):
    class Meta:
        model=Student
        fields=['student_name','counsillor_name']
    
    widgets={
        'student_name':forms.CharField(max_length=100),
        'counsillor_name':forms.Select(choices=[('rekha','rekha'),('rekhila','rekhila'),('savitha','savitha'),('sangeetha','sangeetha')]),
    }
        
class CounsillorsForm(forms.ModelForm):
    class Meta:
        model=Counsillors
        fields='__all__'
    widgets={
         'name': forms.Select(choices=[('rekha','rekha'),('rekhila','rekhila'),('savitha','savitha'),('sangeetha','sangeetha')]),
    }
        
class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields=['fac_user','name']
        
    widgets={
        'name':forms.CharField(max_length=100),
    }
        
# class AttendenceForm(forms.ModelForm):
#     class Meta:
#         model=Attendence
#         fields=['updated_date']
        
class AttendenceReportForm(forms.ModelForm):
    class Meta:
        model=AttendenceReport
        fields=['status','updated_at']
        
    widgets={
        'status':forms.Select(choices=[('attendence 20%','attendence 20%'),('attendence 50%','attendence 50%'),('attendence 100%','attendence 100%')])
    }