from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import PhoneNumberIntegerField,CostumUserForm,CourseForm,RepeatedUserForm,RegisteredForm
from . models import  CustomUser,Courses,RepeatedUser,Enquery
from django.http import JsonResponse
import json
# Create your views here.

def home_view(request):
    if request.POST:
        print("request is post")
        form=PhoneNumberIntegerField(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form=PhoneNumberIntegerField()
        return render(request,'home.html',{'form':form})
    
def form2_view(request):
    if request.POST:
        print("request is post")
        form=CostumUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        print("req is at get")
        form=CostumUserForm()
        return render(request,'form2.html',{'form':form})
    
def course_view(request):
    if request.POST:
        print("req is at post in course")
        coursetype=request.POST.get('course_type')
        courseduration=request.POST.get('course_duration')
        coursename=request.POST.get('course_name')
        updatedat=request.POST.get('updated_at')
        course_data=Courses(course_type=coursetype,course_duration=courseduration,course_name=coursename,updated_at=updatedat)
        if course_data:
            print("form validated")
            course_data.save()
            return redirect('base')
    else:
        print("req is at get in course")
        form=CourseForm()
        return render(request,'course.html',{'form':form})
    
def repeated_user_view(request):
    if request.POST:
        name=request.POST.get('name')
        last_enquiry_date=request.POST.get('last_enquiry_date')
        phone_number=request.POST.get('phone_number')   
        repeated_user_data=RepeatedUser(name=name, last_enquiry_date=last_enquiry_date, phone_number=phone_number)
        if repeated_user_data:
          repeated_user_data.save()
          return redirect('base')
    else:
        form=RepeatedUserForm()
        return render(request,'repeated_user.html',{'form':form})
    
def Registerationform(request):
    if request.POST:
      print("req is at post")
      name = request.POST.get('name') 
      address1 = request.POST.get('address1'),
      address2 = request.POST.get('address2'),
      address3 = request.POST.get('address3'),
      address4 = request.POST.get('address4')
      address5 = request.POST.get('address5')
      full_address = f"{address1} {address4} {address3} Pin Code:{address5}"
      email_id = request.POST.get('email_id')
      gender = request.POST.get('gender')
      college = request.POST.get('college')
      mode_of_class = request.POST.get('mode')
      guardian_name = request.POST.get('guardian_name')
      alternative_phone_no = request.POST.get('alt_contact')
      technical_skills = request.POST.get('technical_skills')
      address = full_address
      profile_pic = request.FILES.get('photo')    
      consultant_name = request.POST.get('consultant_name')
      reference_name = request.POST.get('reference_name')
      reference_contact_number = request.POST.get('reference_num')
      status_of_enquiry = 'Registered'
      result=Enquery(email_id=email_id,gender=gender, college=college, mode_of_class=mode_of_class, guardian_name=guardian_name, alternate_phone_number=alternative_phone_no, technical_skills=technical_skills, address=address, profile_pic=profile_pic, consultant_name=consultant_name, reference_name=reference_name, reference_contact_number=reference_contact_number, status_of_enquiry=status_of_enquiry, name=name)
      if result:
        print("validating form")
        result.save()
        return redirect('https://cbtech.in/')
    else:
        print("req in else")
        form=RegisteredForm()
       # return render(request,'registration.html',{'form':form})
        custom_users = CustomUser.objects.filter(staff_type='counsellor')
        user_choices = [(user.first_name, user.first_name) for user in custom_users]
       # data_dict = dict(user_choices)
        #user_choices = json.dumps(data_dict)
        return render(request, 'registration.html',context={'form':form, 'user_choices':user_choices})

def get_data(request):
    data=list(Enquery.objects.all().values())
    return JsonResponse({'data':data})
    
    
def base_view(request):
    return render(request,'base.html')
            
