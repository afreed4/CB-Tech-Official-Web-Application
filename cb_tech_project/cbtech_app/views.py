from django.contrib.auth import get_user_model
from .forms import *
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
import json
from import_export.formats.base_formats import XLS, XLSX, CSV
import phonenumbers
from django.core import serializers
from django.http import JsonResponse
from .models import repeated_user

def format_phone_number(phone_number):
    parsed_number = phonenumbers.parse(str(phone_number), "IN")  # Change "US" to the appropriate country code
    return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

User = get_user_model()

# Create your views here.
def home(request):
    return render(request,'index.html')


# User login



@login_required(login_url='/')
def staff_dash(request):
    return render(request,'staff_dash/staff-dshboard.html')

@login_required(login_url='/')
def admin_dash(request):
    return render(request, 'admin_dash/admin-dashboard.html')


# Enquiry Registeration

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffdash')
        else:
            messages.info('Check the details and try again!')
            return redirect('enquiryform')
    else:
        form = EnquiryForm()
        dict = {'form':form}
    return render(request,'enquiryform.html',context=dict)


# Staff/Admin Login

def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.staff_type == 'admin':
             login(request, user)
             return redirect('admin_home')
        elif user is not None and user.is_staff == True:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.warning(request,'Check username and password ¯\_(ツ)_/¯')
            return redirect('loginadmin')
    return render(request,'admin_dash/admin-login.html')

def accountant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.staff_type == 'accountant':
             login(request, user)
             return redirect('accountant_manage')
        else:
            messages.warning(request,'Check username and password ¯\_(ツ)_/¯')
            return redirect('accountantlogin')
    return render(request,'accountant_dash/accountant-login.html')

def loginstaff(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.staff_type == 'counsellor':
             login(request, user)
             return redirect('staff_home')
        elif user is not None and user.staff_type == 'faculty':
            login(request, user)
            return redirect('staff_home')
        elif user is not None and user.staff_type == 'marketing manager':
            login(request, user)
            return redirect('staff_home')
        else:
            messages.warning(request,'Check username and password ¯\_(ツ)_/¯')
            return redirect('loginstaff')
    return render(request,'staff_dash/staff-login.html')

@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def ImportEnquiryData(request):
    if request.method == 'POST':
        file_format = request.FILES['myfile'].name.split('.')[-1]
        if file_format in ['xls', 'xlsx', 'csv']:
            lead_type = request.POST['drop']
            enquirydate = request.POST['date_of_enquiry']

            data = request.FILES['myfile']
            if file_format == 'csv':
                dataset = pd.read_csv(data)
            elif file_format in ['xls', 'xlsx']:
                dataset = pd.read_excel(data)

            try:
                enquiry_data_list = []
                
                enquiry_model_fields = [field.name for field in Enquiry._meta.fields]
                print(enquiry_model_fields)

                # Iterate through each row in the dataset
                for index, row in dataset.iterrows():
                    # Create a dictionary to hold the column values for this row
                    enquiry_data = {}

                    # Iterate through the columns and their values in the current row
                    for column in dataset.columns:
                        if column in enquiry_model_fields:
                            enquiry_data[column] = row[column]
                    enquiry_data['lead_type'] = lead_type
                    enquiry_data['date_of_enquiry'] = enquirydate
                    
                    # Add the dictionary to the list
                    enquiry_data_list.append(enquiry_data)

                # Iterate through the list of dictionaries and save data to the Enquiry model
                for enquiry_data in enquiry_data_list:
                    exsist_objects = Enquiry.objects.filter(phone_number=enquiry_data['phone_number'])
                    if exsist_objects:
                        for exsist_object in exsist_objects:
                            name = exsist_object.name
                            phonenumber = exsist_object.phone_number
                            last_enquiry_date = exsist_object.date_of_enquiry
                            repeated = repeated_user(name=name, last_enquiry_date=last_enquiry_date, phone_number=phonenumber)
                            repeated.save()
                    else:
                        enquiry = Enquiry(**enquiry_data)
                        enquiry.save()

                # After processing all entries, redirect
                return redirect('manage_enquiry')
            except KeyError:
                 messages.error(request,"Check the value of the input fields in the file ")
                 return render(request, 'importing.html')

    return render(request, 'importing.html')

@login_required(login_url='/')
def staffImportEnquiryData(request):
    if request.method == 'POST':
        file_format = request.FILES['myfile'].name.split('.')[-1]
        if file_format in ['xls', 'xlsx', 'csv']:
            lead_type = request.POST['drop']
            enquirydate = request.POST['date_of_enquiry']

            data = request.FILES['myfile']
            if file_format == 'csv':
                dataset = pd.read_csv(data)
            elif file_format in ['xls', 'xlsx']:
                dataset = pd.read_excel(data)

        try:
                enquiry_data_list = []
                
                enquiry_model_fields = [field.name for field in Enquiry._meta.fields]
                print(enquiry_model_fields)

                # Iterate through each row in the dataset
                for index, row in dataset.iterrows():
                    # Create a dictionary to hold the column values for this row
                    enquiry_data = {}

                    # Iterate through the columns and their values in the current row
                    for column in dataset.columns:
                        if column in enquiry_model_fields:
                            enquiry_data[column] = row[column]
                    enquiry_data['lead_type'] = lead_type
                    enquiry_data['date_of_enquiry'] = enquirydate

                    # Add the dictionary to the list
                    enquiry_data_list.append(enquiry_data)

                # Iterate through the list of dictionaries and save data to the Enquiry model
                for enquiry_data in enquiry_data_list:
                    exsist_objects = Enquiry.objects.filter(phone_number=enquiry_data['phone_number'])
                    if exsist_objects:
                        for exsist_object in exsist_objects:
                            name = exsist_object.name
                            phonenumber = exsist_object.phone_number
                            last_enquiry_date = exsist_object.date_of_enquiry
                            repeated = repeated_user(name=name, last_enquiry_date=last_enquiry_date, phone_number=phonenumber)
                            repeated.save()
                    else:
                        enquiry = Enquiry(**enquiry_data)
                        enquiry.save()
                return redirect('staff_manage_enquiry')
        except KeyError:
                messages.error(request,"Check the value of the input fields in the file ")
                return render(request, 'import.html')

    return render(request, 'import.html')


def publicEnquiry(request):
    if request.method == 'POST':
        names=request.POST.get('Name')
        email=request.POST.get('email')
        phoneno=request.POST.get('contact')
        alt_no =request.POST.get('altcontact')
        qualif =request.POST.get('quali')
        passout=request.POST.get('pass')
        skill=request.POST.get('skills')
        consultant=request.POST.get('consultant')
        office = request.POST.get('office')

        public=Enquiry(
            name=names,
            email_id=email,
            phone_number=phoneno,
            alternate_phone_number = alt_no,
            qualification = qualif,
            year_of_pass=passout,
            technical_skills=skill,
            consultant_name=consultant,
            office = office,
        )
        public.save()   
        return redirect('https://cbtech.co.in/')
    custom_users = CustomUser.objects.filter(staff_type='counsellor')
    user_choices = [(user.first_name, user.first_name) for user in custom_users]
    data_dict = dict(user_choices)
    user_choices = json.dumps(data_dict)
    return render(request, 'contactus.html',context={'user_choices':user_choices})


    
    

def Registerationform(request):
    custom_users = CustomUser.objects.filter(staff_type='Counsellor')
    #print("custom_users",custom_users)
    user_choices = [user.first_name for user in custom_users]
    
    #data_dict = dict(user_choices)
    # user_choices = json.dumps(data_dict)
    print(custom_users)
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
      office = request.POST.get('office')
      phone_number = request.POST.get('phone_num')
      qualification = request.POST.get('qualification')
      course_name = request.POST.get('course_name')
      course_duration = request.POST.get('course_duration')
      course_type = request.POST.get('course_type')
      status_of_enquiry = 'Registered'
      result=Enquiry(email_id=email_id,gender=gender, college=college, mode_of_class=mode_of_class, guardian_name=guardian_name, alternate_phone_number=alternative_phone_no, technical_skills=technical_skills, address=address, profile_pic=profile_pic, consultant_name=consultant_name, reference_name=reference_name, reference_contact_number=reference_contact_number, status_of_enquiry=status_of_enquiry, name=name, office=office, phone_number=phone_number, qualification=qualification, course=course_name, course_duration=course_duration, course_type=course_type)
      if result:
        print("validating form")
        result.save()
        return redirect('https://cbtech.in/')
    else:
        print("req in else")
        form=RegisteredForm()
        return render(request,'registration.html',{'form':form, 'user_choices':user_choices})
    #return render(request,'registration.html',{'user_choices':user_choices})
    
    