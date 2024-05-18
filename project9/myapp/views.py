from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect 
from django.contrib.auth import logout, authenticate, login 
from .models import customuser, Staffs, Students, AdminHOD 
from django.contrib import messages 
  
#from .forms import  EditStudentForm 
  
from .models import customuser, Staffs, Students, Attendance, AttendanceReport

def admin_home(request):
    all_student_count = Students.objects.all().count() 
    #subject_count = Subjects.objects.all().count() 
    #course_count = Courses.objects.all().count() 
    staff_count = Staffs.objects.all().count() 
    #course_all = Courses.objects.all() 
    #course_name_list = [] 
    #subject_count_list = [] 
    #student_count_list_in_course = [] 
    student_attendance_present_list=[] 
    student_attendance_leave_list=[] 
    student_name_list=[] 
  
    students = Students.objects.all() 
    for student in students: 
        attendance = AttendanceReport.objects.filter(student_id=student.id, 
                                                     status=True).count() 
        absent = AttendanceReport.objects.filter(student_id=student.id, 
                                                 status=False).count() 
        #leaves = LeaveReportStudent.objects.filter(student_id=student.id, 
                                                 #  leave_status=1).count() 
        student_attendance_present_list.append(attendance) 
        student_attendance_leave_list.append(absent) 
        student_name_list.append(student.admin.first_name) 
  
  
    context={ 
        "all_student_count": all_student_count, 
        #"subject_count": subject_count, 
        #"course_count": course_count, 
        "staff_count": staff_count, 
        #"course_name_list": course_name_list, 
       # "subject_count_list": subject_count_list, 
        #"student_count_list_in_course": student_count_list_in_course, 
        #"subject_list": subject_list, 
       # "student_count_list_in_subject": student_count_list_in_subject, 
        #"staff_attendance_present_list": staff_attendance_present_list, 
       # "staff_attendance_leave_list": staff_attendance_leave_list, 
        #"staff_name_list": staff_name_list, 
        "student_attendance_present_list": student_attendance_present_list, 
        "student_attendance_leave_list": student_attendance_leave_list, 
        "student_name_list": student_name_list, 
    } 
    return render(request, "home.html", context) 


def add_staff(request): 
    return render(request, "add_staff_template.html") 
  
  
def add_staff_save(request): 
    if request.method != "POST": 
        messages.error(request, "Invalid Method ") 
        return redirect('add_staff') 
    else: 
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        address = request.POST.get('address') 
  
        try: 
            user = customuser.objects.create_user(username=username, 
                                                  password=password, 
                                                  email=email, 
                                                  first_name=first_name, 
                                                  last_name=last_name, 
                                                  user_type=2) 
            user.staffs.address = address 
            user.save() 
            messages.success(request, "Staff Added Successfully!") 
            return redirect('add_staff') 
        except: 
            messages.error(request, "Failed to Add Staff!") 
            return redirect('add_staff') 
        
        
def loginUser(request): 
    return render(request, 'login_page.html') 
  
def doLogin(request): 
      
    print("here") 
    email_id = request.GET.get('email') 
    password = request.GET.get('password') 
    # user_type = request.GET.get('user_type') 
    print(email_id) 
    print(password) 
    print(request.user) 
    if not (email_id and password): 
        messages.error(request, "Please provide all the details!!") 
        return render(request, 'login_page.html') 
  
    user = customuser.objects.filter(email=email_id, password=password).last() 
    if not user: 
        messages.error(request, 'Invalid Login Credentials!!') 
        return render(request, 'login_page.html') 
  
    login(request, user) 
    print(request.user) 
  
    if user.user_type == customuser.STUDENT: 
        return redirect('student_home/') 
    elif user.user_type == customuser.STAFF: 
        return redirect('staff_home/') 
    elif user.user_type == customuser.HOD: 
        return redirect('admin_home/') 
  
    return render(request, 'home.html') 
  

def registration(request): 
    return render(request, 'registration.html') 

def doRegistration(request): 
    first_name = request.GET.get('first_name') 
    last_name = request.GET.get('last_name') 
    email_id = request.GET.get('email') 
    password = request.GET.get('password') 
    confirm_password = request.GET.get('confirmPassword') 
  
    print(email_id) 
    print(password) 
    print(confirm_password) 
    print(first_name) 
    print(last_name) 
    if not (email_id and password and confirm_password): 
        messages.error(request, 'Please provide all the details!!') 
        return render(request, 'registration.html') 
      
    if password != confirm_password: 
        messages.error(request, 'Both passwords should match!!') 
        return render(request, 'registration.html') 
  
    is_user_exists = customuser.objects.filter(email=email_id).exists() 
  
    if is_user_exists: 
        messages.error(request, 'User with this email id already exists. Please proceed to login!!') 
        return render(request, 'registration.html') 
  
    user_type = get_user_type_from_email(email_id) 
  
    if user_type is None: 
        messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'") 
        return render(request, 'registration.html') 
  
    username = email_id.split('@')[0].split('.')[0] 
  
    if customuser.objects.filter(username=username).exists(): 
        messages.error(request, 'User with this username already exists. Please use different username') 
        return render(request, 'registration.html') 
  
    user = customuser() 
    user.username = username 
    user.email = email_id 
    user.password = password 
    user.user_type = user_type 
    user.first_name = first_name 
    user.last_name = last_name 
    user.save() 
      
    if user_type == customuser.STAFF: 
        Staffs.objects.create(admin=user) 
    elif user_type == customuser.STUDENT: 
        Students.objects.create(admin=user) 
    elif user_type == customuser.HOD: 
        AdminHOD.objects.create(admin=user) 
    return render(request, 'login_page.html') 


def get_user_type_from_email(email_id): 
    """ 
    Returns CustomUser.user_type corresponding to the given email address 
    email_id should be in following format: 
    '<username>.<staff|student|hod>@<college_domain>' 
    eg.: 'abhishek.staff@jecrc.com' 
    """
  
    try: 
        email_id = email_id.split('@')[0] 
        email_user_type = email_id.split('.')[1] 
        return customuser.EMAIL_TO_USER_TYPE_MAP[email_user_type] 
    except: 
        return None