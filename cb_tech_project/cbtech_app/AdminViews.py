from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from cbtech_app.models import CustomUser,Enquiry,Courses
from .forms import EnquiryForm,RegisteredForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.http import JsonResponse
import json
from django.core.exceptions import *
from .models import repeated_user
from django.contrib.auth import authenticate
User = get_user_model()
current_date = datetime.now()
previous_month = current_date - relativedelta(months=1)
timezone.now().date()


def filter_by_status(status_of_enquiry):
    registered = Enquiry.objects.filter(status_of_enquiry = status_of_enquiry).order_by('-enquiry_id')
    return registered



@login_required(login_url='/')
def admin_home(request,month_enq=current_date.month,year_enq=current_date.year,month_cons=current_date.month,year_cons=current_date.year):
    enquiry_count_chart = Enquiry.objects.filter(date_of_enquiry__month=month_enq,date_of_enquiry__year=year_enq).count()
    staff_count = User.objects.all().count()
    course_count = Courses.objects.all().count()
    registered_count_chart = Enquiry.objects.filter(status_of_enquiry = 'Registered',date_of_registration__month=month_enq,date_of_registration__year=year_enq).order_by('-enquiry_id').count()
    Enquiries = Enquiry.objects.all().order_by('-enquiry_id')[:3]
    enquiry_count = Enquiry.objects.filter().count()
    registered_count = Enquiry.objects.filter(status_of_enquiry = 'Registered').order_by('-enquiry_id').count()





    counsellors = User.objects.filter(staff_type = 'counsellor')
    counsellor_registeration_count=[]
    counsellor_name_list = []
    for counsellor in counsellors:
        counsellor_name_list.append(counsellor.first_name) 
        registerations = Enquiry.objects.filter(consultant_name=counsellor.first_name,status_of_enquiry='Registered',date_of_registration__month = month_cons,date_of_registration__year=year_cons)
        count = registerations.count()
        counsellor_registeration_count.append(count)




    context = {
        'enquiry_count':enquiry_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'registered_count':registered_count,
        'Enquiries':Enquiries,
        'counsellor_name_list':counsellor_name_list,
        'counsellor_registeration_count':counsellor_registeration_count,
        'month_enq':month_enq,
        'year_enq':year_enq,
        'month_cons':month_cons,
        'year_cons':year_cons,
        'enquiry_count_chart':enquiry_count_chart,
        'registered_count_chart':registered_count_chart,

    }
    
    return render(request, "admin_template/home_content.html",context)

@login_required(login_url='/')
def add_staff(request):
    return render(request, "admin_template/add_staff_template.html")

@login_required(login_url='/')
def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
         # form.save()
        username = request.POST['username']
        password = request.POST['password']
        existing_user=User.objects.filter(username=username).first()
        
        if existing_user:
            user=authenticate(username=username, password=password)
           
            if user is not None:
             messages.error(request, "Username or Password allready exists Try another Username or Password")
             return redirect('add_staff')
            else:
                messages.error(request,"Username or Password allready exists Try another Username or Password")
                return redirect('add_staff')
        else:
       
         first_name = request.POST['first_name']
         second_name = request.POST['last_name']
         staff_type = request.POST['staff_type']
         contact_number =request.POST['contact_number']
         email = request.POST['email']
        
        
         User.objects.create_user(username=username, password=password, staff_type=staff_type, contact_number=contact_number,first_name=first_name,last_name=second_name,email=email)
         return redirect('admin_home')
        # Handle successful registration (e.g., redirect to a success page)

@login_required(login_url='/')
def manage_staff(request):
    CustomUser = User.objects.all()
    context = {
        "staffs": CustomUser
    }
    return render(request, "admin_template/manage_staff_template.html", context)

@login_required(login_url='/')
def edit_staff(request, staff_id):
    staff = User.objects.get(id=staff_id)

    context = {
        "staff": staff,
        "id": staff_id,
    }
    return render(request, "admin_template/edit_staff_template.html", context)

@login_required(login_url='/')
def edit_staff_save(request, user_id):
    if request.POST:
       # return HttpResponse("<h2>Method Not Allowed</h2>")
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        staff_type = request.POST.get('staff_type')
        password = request.POST.get('password')
        staff = User.objects.get(id=staff_id)
        
         # INSERTING into Customuser Model
        staff.first_name = first_name
        staff.last_name = last_name
        staff.contact_number = contact_number
        staff.staff_type = staff_type
        staff.set_password(password)
        staff.save()
        messages.success(request, "Staff Updated Successfully.")
        return redirect('edit_staff_save',user_id=staff_id)
    else:
           # messages.error(request, "Failed to Update Staff.")
            user=User.objects.get(id=user_id)
            context = {
                "staff": user,
                "id": user.id,
            }
            return render(request, "admin_template/edit_staff_template.html", context)


@login_required(login_url='/')
def delete_staff(request, staff_id):
    staff = CustomUser.objects.filter(id=staff_id)
    staff.delete()
    messages.success(request, "Staff Deleted Successfully.")
    return redirect('manage_staff')

#--------------------------------(end of staff section)-------------------------------

@login_required(login_url='/')
def add_course(request):
    return render(request, "admin_template/add_course_template.html")

@login_required(login_url='/')
def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        # course = request.POST.get('course')
        course_name = request.POST.get('course')
        course_type = request.POST.get('course_type')
        course_duration = request.POST.get('course_duration')
        try:
            course_model = Courses(course_name=course_name,course_type=course_type,course_duration=course_duration)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('manage_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')

@login_required(login_url='/')
def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'admin_template/manage_course_template.html',context)

@login_required(login_url='/')
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        "course": course,
        "id": course_id
    }
    return render(request, 'admin_template/edit_course_template.html', context)

@login_required(login_url='/')
def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('courseId')
        course_name = request.POST.get('course')
        course_type = request.POST.get('course_type')
        course_duration = request.POST.get('course_duration')
        try:
            course_model = Courses.objects.get(id=course_id)
            course_model.course_name = course_name
            course_model.course_type = course_type
            course_model.course_duration = course_duration
            course_model.save()
            messages.success(request, "Course Edit Successfully!")
            return redirect('manage_course')
        except:
            messages.error(request, "Failed to Edit Course!")
            return redirect('edit_course'+course_id)


@login_required(login_url='/')
def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')

#--------------------------------(end of course section)-------------------------------

@login_required(login_url='/')
def add_Enquiry(request):
    form = EnquiryForm()
    context = {
        "form": form,
    }
    return render(request, 'admin_template/add_enquiry_template.html', context)



@login_required(login_url='/')
def add_enquiry_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_enquiry')
    else:
            phonenumber = request.POST['phone_number']
            exsist_objects = Enquiry.objects.filter(phone_number=phonenumber)
            if exsist_objects:
                for exsist_object in exsist_objects:
                    name=exsist_objects.name
                    phonenumber = exsist_object.phone_number
                    last_enquiry_date = exsist_object.date_of_enquiry
                    repeated_user = repeated_user(name=name,last_enquiry_date=last_enquiry_date,phone_number=phonenumber)
                    repeated_user.save()
            else:
                form = EnquiryForm(request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('manage_enquiry')
                else:
                    messages.error(request,'Check the details and try again!')
                    form = EnquiryForm()
                    context = {
                        "form": form,
                    }
                    return render(request, 'admin_template/add_enquiry_template.html', context)




@login_required(login_url='/')
def manage_enquiry(request):
    students = Enquiry.objects.all().order_by('-enquiry_id')
    context = {
        "Enquiries": students
    }
    return render(request, 'admin_template/manage_enquiry_template.html',context)

@login_required(login_url='/')
def edit_enquiry(request, enquiry_id):
    # Adding Student ID into Session Variable

    enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
    form = EnquiryForm(instance=enquiry,user=request.user)


    context = {
        "id": enquiry_id,
        "form": form
    }
    return render(request, "admin_template/edit_enquiry_template.html", context)


@login_required(login_url='/')
def edit_enquiry_save(request,enquiry_id):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
        form = EnquiryForm(request.POST,instance = enquiry,user=request.user)
        if form.is_valid():
            form.save()
            status = request.POST.get('status_of_enquiry')
            if status == 'Registered':
                form = RegisteredForm(instance=enquiry)
                context = {
                    "id": enquiry_id,
                    "form": form
                }
                return render(request, "admin_template/edit_registeration_template.html", context)
            return redirect('manage_enquiry')
        else:
            messages.error(request,'Check the details and try again!')
            context = {
            "id": enquiry_id,
            "form": form,
            }
            return render(request, "admin_template/edit_enquiry_template.html", context)
            

@login_required(login_url='/')
def delete_enquiry(request, enquiry_id):
   enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
   try:
        enquiry.delete()
        messages.error(request, "Enquiry Deleted Successfully.")
        return redirect('manage_enquiry')
   except:
        messages.error(request, "Failed to Delete Enquiry.")
        return redirect('manage_enquiry')


@login_required(login_url='/')
def manage_registeration(request):
    registered = filter_by_status('Registered')
    context = {
        "registered": registered
    }
    return render(request, 'admin_template/manage_registeration_template.html',context)

@login_required(login_url='/')
def edit_registeration(request,enquiry_id):
    enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
    form = RegisteredForm(instance=enquiry)
    context = {
        "id": enquiry_id,
        "form": form
    }
    return render(request, "admin_template/edit_registeration_template.html", context)

@login_required(login_url='/')
def edit_registeration_save(request,enquiry_id):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
        form = RegisteredForm(request.POST,request.FILES,instance=enquiry)
        if form.is_valid():
            form.save()
            status = request.POST.get('status_of_enquiry')
            if status != 'Registered':
                form = EnquiryForm(instance=enquiry)
                context = {
                    "id": enquiry_id,
                    "form": form
                }
                return render(request, "admin_template/edit_enquiry_template.html", context)
            return redirect('manage_registeration')
        else:
            messages.error(request,'Check the details and try again!')
            context = {
            "id": enquiry_id,
            "form": form,
            }
            return render(request, "admin_template/edit_registeration_template.html", context)

@csrf_exempt
@login_required(login_url='/')
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = User.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
@login_required(login_url='/')
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = User.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)






def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'admin_template/admin_profile.html', context)


@login_required(login_url='/')
def edit_self(request):
    current_user = request.user
    staff_id=current_user.id
    staff = User.objects.get(id=staff_id)

    context = {
        "staff": staff,
        "id": staff_id,
    }
    return render(request, "admin_template/edit_staff_template.html", context)

@login_required(login_url='/')
def update_enq_reg(request):
    data_param = request.GET.get('data')
    data = json.loads(data_param)

    month = data['month']
    year = data['year']
    enquiry_count = Enquiry.objects.filter(date_of_enquiry__month=month,date_of_enquiry__year=year).count()
    registered_count = Enquiry.objects.filter(status_of_enquiry = 'Registered',date_of_registration__month=month,date_of_registration__year=year).order_by('-enquiry_id').count()
    data = {'enquiry_count_chart': enquiry_count,'registered_count': registered_count}
    return JsonResponse(data)

@login_required(login_url='/')
def update_cons_reg(request):
    data_param = request.GET.get('data')
    data = json.loads(data_param)

    month = data['month']
    year = data['year']
    counsellors = User.objects.filter(staff_type = 'counsellor')
    counsellor_registeration_count=[]
    counsellor_name_list = []
    for counsellor in counsellors:
        counsellor_name_list.append(counsellor.first_name) 
        registerations = Enquiry.objects.filter(consultant_name=counsellor.first_name,status_of_enquiry='Registered',date_of_registration__month = month,date_of_registration__year=year)
        count = registerations.count()
        counsellor_registeration_count.append(count)
    data = {'counsellor_name_list': counsellor_name_list,'counsellor_registeration_count': counsellor_registeration_count}
    return JsonResponse(data)

@login_required
def repeated_user_view(request):
    repeated_users = repeated_user.objects.all()
    context = {
        "repeated_users": repeated_users,
    }
    return render(request,"admin_template/view_repeated.html", context)


@login_required
def get_staff_details(request):
    details=User.objects.all()
    specific_user=User.objects.get(id=5)
    username=specific_user.username
    
    return render(request,"admin_template/test.html",{'details':details, 'specific_user':specific_user ,'username':username})