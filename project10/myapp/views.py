from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . forms import StudentForm,FacultyForm,CounsillorsForm,AttendenceReportForm,SighnupForm,LoginForm
from . models import Student,Faculty,Counsillors,Attendence,AttendenceReport
from django.http import HttpResponse
from django.db import IntegrityError
# Create your views here.


def  home_view(request):
    return render(request,'home.html')

def Faculy_sighnup_view(request):
    if request.POST:
        form=SighnupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_home')
    else:
        form=SighnupForm()
    return render(request,'faculty_register.html',{'form':form})

def Faculty_login_view(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password);
            if user:
                login(request,user)
                return redirect('faculty_home')
            else:
                return render(request,'faculty_login.html',{'form':form})
    else:
        form=LoginForm()
    return render(request,'faculty_login.html',{'form':form})
 
def Counsillor_sighnup_view(request):
    if request.POST:
        form=SighnupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counsillor_home')
    else:
        form=SighnupForm()
    return render(request,'counsillor_register.html',{'form':form}) 

def Counsillor_login_view(request):
     if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password);
            if user:
                login(request,user)
                return redirect('counsillor_home')
            else:
                return render(request,'faculty_login.html',{'form':form})
     else:
        form=LoginForm()
     return render(request,'counsillor_login.html',{'form':form})

def add_student_view(request):
    if request.POST:
        form=StudentForm(request.POST)
        if form.is_valid():
            print("form validated")
            name=request.POST.get('name')
            cousnillor_name=request.POST.get('counsellor')
            print(name)
            print("got the cleaned data")
            form2=Student(student_name=name)
            form3=Counsillors(name=cousnillor_name)
           
            print("the form2 is addedd to the DB")
            form3.save()
            form2.save()
            print("form2 saved")
            return redirect('counsillor_home')
    else:
        form=StudentForm()
        return render(request,'add_student.html',{'form':form})

def faculty_home(request):
    student_data=Student.objects.all()
    return render(request,'faculty_home.html',{'student_data':student_data})

def attendence_report_view(request,id_of_attendence):
    if request.POST:
      report=Attendence.objects.filter(id_of_attendence=id_of_attendence)
      print(report)
      return render(request,'attendence_report.html',{'report':report})
    else:
       return render(request,'faculty_home.html',{'id_of_attendence':id_of_attendence})

def attendence_view(request):
    if request.POST:
        date=request.POST.get('date')
        print("date goted")
        status=request.POST.get('value')
        print("status goated")
        form=Attendence(updated_date=date,status=status)
        
        form.save()
        print("form saved")
        return redirect('attendance_report')
    return render(request,'faculty_home.html')



def counsillor_home(request):
    return render(request,'counsillor_home.html')