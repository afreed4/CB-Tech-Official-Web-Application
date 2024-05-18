from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from cbtech_app.models import CustomUser
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate, login,logout

User = get_user_model()

from cbtech_app.models import CustomUser,  Courses, Enquiry

def filter_by_lead(lead_type):
    leads = Enquiry.objects.filter(lead_type = lead_type)
    return leads

@login_required(login_url='/')
def staff_home(request):
    if request.user.is_authenticated:
        username=request.user.username
        naukri_count = filter_by_lead('Naukri').count()
        apna_count = filter_by_lead('Apna').count()
        quicker_count = filter_by_lead('Quicker').count()
        linkedin_count = filter_by_lead('LinkedIn').count()
       # Enquiries = Enquiry.objects.all().order_by('-enquiry_id')[:3]
        facultys=Enquiry.objects.filter(faculty_name=username).order_by('-enquiry_id')[:3]
        student_name=facultys.values_list('name',flat=True)
        Enquiries = Enquiry.objects.filter(name__in=student_name).order_by('-enquiry_id')[:3]
        naukri = filter_by_lead('Naukri')
        apna = filter_by_lead('Apna')
        quicker = filter_by_lead('Quicker')
        linkedin = filter_by_lead('LinkedIn')

        context = {
            'naukri_count':naukri_count,
            'apna_count':apna_count,
            'quicker_count':quicker_count,
            'linkedin_count':linkedin_count,
            'Enquiries':Enquiries,
        }

        return render(request, "staff_template/staff_home_template.html",context)

@login_required(login_url='/')
def staff_add_Enquiry(request):
    form = EnquiryForm()
    context = {
        "form": form,
    }
    return render(request, 'staff_template/add_enquiry_template.html', context)


@login_required(login_url='/')
def staff_add_enquiry_save(request):
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
                    return render(request, 'staff_template/add_enquiry_template.html', context)



@login_required(login_url='/')
def staff_manage_enquiry(request):
    if request.user.is_authenticated:
        username=request.user.username
        facultys=Enquiry.objects.filter(faculty_name=username).order_by('-enquiry_id')
        student_name=facultys.values_list('name',flat=True)
        students = Enquiry.objects.filter(name__in=student_name).order_by('-enquiry_id')
        print(students)
        context = {
            "Enquiries": students
        }
        return render(request, 'staff_template/staff_manage_enquiry.html',context)

@login_required
def course_completion(request):
    if request.user.is_authenticated:
        username=request.user.username
        facultys=Enquiry.objects.filter(faculty_name=username).order_by('-enquiry_id')
        completion_list=facultys.values_list('course_completion',flat=True)
        completion_list = Enquiry.objects.filter(course_completion__in=completion_list).order_by('-enquiry_id')
       
        paginator=Paginator(completion_list,15)
        page=request.GET.get('page')
        
        try:
            items=paginator.page(page)
        except PageNotAnInteger:
            items=paginator.page(1)
        except EmptyPage:
            items=paginator.page(paginator.num_pages)
        return render(request,'staff_template/completion.html',{'items':items})

@login_required
def attendance_view(request,id):
     if request.POST:
        date=request.POST.get('date')
        print("date goted")
        status=request.POST.get('value')
        print("status goated")
        enquiry=get_object_or_404(Enquiry, enquiry_id=id)
        if status=='Present':
            form=Attendence(updated_date=date,present=status,connection=enquiry)
            form.save()
            messages.success(request,"Attendance Taken SuccessFully !!")
            return redirect('take_attendance')
        elif status=='Absent':
             form2=Attendence(updated_date=date,absent=status,connection=enquiry)
             form2.save()
             messages.success(request,"Attendance Taken SuccessFully !!")
             print("form saved")
             return redirect('take_attendance')
        else:
             messages.error(request,"Somthing Went Wrong Please Try Again !!")
             return redirect('take_attendance',id=id)
     return render(request,'staff_template/staff_edit_enquiry.html')


def attendance_report(request):
    return render(request,'staff_template/attendance.html')

@login_required
def attendance_report_view(request, id):
    print(id)
    enquiry =get_object_or_404(Enquiry, enquiry_id=id)
    
    attendance_record=Attendence.objects.filter(connection__enquiry_id=id)
    print(attendance_record)
    print(enquiry)
    paginator=Paginator(attendance_record,15)
    page=request.GET.get('page')
    #print(result.attendence_date)
   
    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items=paginator.page(1)
    except EmptyPage:
        items=paginator.page(paginator.num_pages)
    return render(request, 'staff_template/attendance_report.html', {'items':items, 'enquiry':enquiry})

    #   report=Attendence.objects.filter(id_of_attendence=id_of_attendence)
    #   if result:
    #         print("in result")
    #         return render(request,'staff_template/attendance_report.html',{'report':report})
     
         
    
@login_required(login_url='/')
def staff_edit_enquiry(request, enquiry_id):
    # Adding Student ID into Session Variable

    enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
    form = EnquiryForm(instance=enquiry, user=request.user)
    # Filling the form with Data from Database

    context = {
        "id": enquiry_id,
        "form": form
    }
    return render(request, "staff_template/staff_edit_enquiry.html", context)





@login_required(login_url='/')
def staff_edit_enquiry_save(request,enquiry_id):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
        form = EnquiryForm(request.POST,instance=enquiry, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('staff_manage_enquiry')
        else:
            messages.error(request,'Check the details and try again!')
            context = {
            "id": enquiry_id,
            "form": form,
            }
            return render(request, "staff_template/staff_edit_enquiry.html", context)
        
@login_required(login_url='/')        
def staff_update_password(request):
    form = Update_password_form()
    current_user = request.user
    context = {
        'form':form,
        'id':current_user.id,
    }
    return render(request,"staff_template/staff_update_password.html",context)

@login_required(login_url='/')
def staff_update_password_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_update_password')
    else:
        current_user = request.user
        form = Update_password_form()
        user = User.objects.get(id=current_user.id)
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        repeat_new_password = request.POST['repeat_new_password']
        if (new_password == repeat_new_password):
            if user.check_password(current_password):
            # Set a new password
                user.password = make_password(new_password)
                user.save()
                messages.success(request,'Password Updated Successfully')
                context = {
                    'form':form,
                    'id':current_user.id,
                }
                return render(request,"staff_template/staff_update_password.html",context)
            else:
                messages.error(request,'Check your current password')
                context = {
                    'form':form,
                    'id':current_user.id,
                }
                return render(request,"staff_template/staff_update_password.html",context)
        else:
            messages.error(request,'New passwords does not match')
            context = {
                'form':form,
                'id':current_user.id,
            }
            return render(request,"staff_template/staff_update_password.html",context)


@login_required(login_url='/')
def add_course(request):
    return render(request, "staff_template/staff_add_course.html")


@login_required(login_url='/')
def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_add_course')
    else:
        # course = request.POST.get('course')
        course_name = request.POST.get('course')
        course_type = request.POST.get('course_type')
        course_duration = request.POST.get('course_duration')
        try:
            course_model = Courses(course_name=course_name,course_type=course_type,course_duration=course_duration)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('staff_manage_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('staff_add_course')

@login_required(login_url='/')     
def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'staff_template/staff_manage_course.html',context)


@login_required(login_url='/')
def edit_course(request,id):
    course = Courses.objects.get(id=id)
    context = {
        "course": course,
        "id": id
    }
    return render(request, 'staff_template/staff_edit_course.html', context)


@login_required(login_url='/')
def edit_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_add_course')
    else:
        # course = request.POST.get('course')
        course_name = request.POST.get('course')
        course_type = request.POST.get('course_type')
        course_duration = request.POST.get('course_duration')
        try:
            course_model = Courses(course_name=course_name,course_type=course_type,course_duration=course_duration)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('staff_manage_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('staff_add_course')