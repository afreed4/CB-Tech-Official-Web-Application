from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage  
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt 
from django.core import serializers 
import json 
  
  
from .models import customuser, Staffs, Students, Attendance, AttendanceReport
  
def staff_home(request): 
    
    # Fetching All Students under Staff 
    print(request.user.id) 
    #subjects = Subjects.objects.filter(staff_id=request.user.id) 
   # print(subjects) 
    course_id_list = [] 
    #for subject in subjects: 
     #   course = Courses.objects.get(id=subject.course_id.id) 
     #   course_id_list.append(course.id) 
  
    final_course = [] 
    # Removing Duplicate Course Id 
    #for course_id in course_id_list: 
       # if course_id not in final_course: 
        #    final_course.append(course_id) 
              
    print(final_course) 
    students_count = Students.objects.count() 
   # subject_count = subjects.count() 
    #print(subject_count) 
    print(students_count) 
      
    # Fetch All Attendance Count 
    attendance_count = Attendance.objects.count() 
      
    # Fetch All Approve Leave 
    # print(request.user) 
    #print(request.user.user_type) 
    staff = Staffs.objects.get(admin=request.user.id) 
    #leave_count = LeaveReportStaff.objects.filter(staff_id=staff.id, 
                                                #  leave_status=1).count() 
  
    # Fetch Attendance Data by Subjects 
    subject_list = [] 
    attendance_list = [] 
   # for subject in subjects: 
    attendance_count1 = Attendance.objects.filter().count() 
    #subject_list.append(subject.subject_name) 
    attendance_list.append(attendance_count1) 
  
    students_attendance = Students.objects.filter(course_id__in=final_course) 
    student_list = [] 
    student_list_attendance_present = [] 
    student_list_attendance_absent = [] 
    for student in students_attendance: 
        attendance_present_count = AttendanceReport.objects.filter(status=True, 
                                                                   student_id=student.id).count() 
        attendance_absent_count = AttendanceReport.objects.filter(status=False, 
                                                                  student_id=student.id).count() 
        student_list.append(student.admin.first_name+" "+ student.admin.last_name) 
        student_list_attendance_present.append(attendance_present_count) 
        student_list_attendance_absent.append(attendance_absent_count) 
  
    context={ 
        "students_count": students_count, 
        "attendance_count": attendance_count, 
        #"leave_count": leave_count, 
        #"subject_count": subject_count, 
        "subject_list": subject_list, 
        "attendance_list": attendance_list, 
        "student_list": student_list, 
        "attendance_present_list": student_list_attendance_present, 
        "attendance_absent_list": student_list_attendance_absent 
    } 
    return render(request, "staff_template/staff_home_template.html", context) 



@csrf_exempt
def get_students(request): 
    
   # subject_id = request.POST.get("subject") 
    #session_year = request.POST.get("session_year") 
  
    # Students enroll to Course, Course has Subjects 
    # Getting all data from subject model based on subject_id 
   # subject_model = Subjects.objects.get(id=subject_id) 
  
   # session_model = SessionYearModel.objects.get(id=session_year) 
  
    students = Students.objects.all()
  
    # Only Passing Student Id and Student Name Only 
    list_data = [] 
  
    for student in students: 
        data_small={"id":student.admin.id, 
                    "name":student.admin.first_name+" "+student.admin.last_name} 
        list_data.append(data_small) 
  
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False) 
  
  
  
def staff_take_attendance(request): 
    #subjects = Subjects.objects.filter(staff_id=request.user.id) 
    #session_years = SessionYearModel.objects.all() 
   # context = { 
       # "subjects": subjects, 
      #  "session_years": session_years 
   # } 
    return render(request, "take_attendance_template.html",) 
  
  
@csrf_exempt
def save_attendance_data(request): 
    
    # Get Values from Staf Take Attendance form via AJAX (JavaScript) 
    # Use getlist to access HTML Array/List Input Data 
    student_ids = request.POST.get("student_ids") 
   # subject_id = request.POST.get("subject_id") 
    attendance_date = request.POST.get("attendance_date") 
    #session_year_id = request.POST.get("session_year_id") 
  
   # subject_model = Subjects.objects.get(id=subject_id) 
    #session_year_model = SessionYearModel.objects.get(id=session_year_id) 
  
    json_student = json.loads(student_ids) 
      
    try: 
        # First Attendance Data is Saved on Attendance Model 
        attendance = Attendance(
                                attendance_date=attendance_date, 
                                                )
                               # session_year_id=session_year_model) 
        attendance.save() 
  
        for stud in json_student: 
            # Attendance of Individual Student saved on AttendanceReport Model 
            student = Students.objects.get(admin=stud['id']) 
            attendance_report = AttendanceReport(student_id=student, 
                                                 attendance_id=attendance, 
                                                 status=stud['status']) 
            attendance_report.save() 
        return HttpResponse("OK") 
    except: 
        return HttpResponse("Error") 
    
    
    
@csrf_exempt
def get_attendance_dates(request): 
      
  
    # Getting Values from Ajax POST 'Fetch Student' 
   # subject_id = request.POST.get("subject") 
    #session_year = request.POST.get("session_year_id") 
  
    # Students enroll to Course, Course has Subjects 
    # Getting all data from subject model based on subject_id 
   # subject_model = Subjects.objects.get(id=subject_id) 
  
   # session_model = SessionYearModel.objects.get(id=session_year) 
    attendance = Attendance.objects.all() 
  
    # Only Passing Student Id and Student Name Only 
    list_data = [] 
  
    for attendance_single in attendance: 
        data_small={"id":attendance_single.id, 
                    "attendance_date":str(attendance_single.attendance_date), 
                    "session_year_id":attendance_single.session_year_id.id} 
        list_data.append(data_small) 
  
    return JsonResponse(json.dumps(list_data), 
                        content_type="application/json", safe=False) 
    
    
@csrf_exempt
def get_attendance_student(request): 
    
    # Getting Values from Ajax POST 'Fetch Student' 
    attendance_date = request.POST.get('attendance_date') 
    attendance = Attendance.objects.get(id=attendance_date) 
  
    attendance_data = AttendanceReport.objects.filter(attendance_id=attendance) 
    # Only Passing Student Id and Student Name Only 
    list_data = [] 
  
    for student in attendance_data: 
        data_small={"id":student.student_id.admin.id, 
                    "name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name, "status":student.status} 
        list_data.append(data_small) 
  
    return JsonResponse(json.dumps(list_data), 
                        content_type="application/json", 
                        safe=False) 
  
  
@csrf_exempt
def update_attendance_data(request): 
    student_ids = request.POST.get("student_ids") 
  
    attendance_date = request.POST.get("attendance_date") 
    attendance = Attendance.objects.get(id=attendance_date) 
  
    json_student = json.loads(student_ids) 
  
    try: 
          
        for stud in json_student: 
            
            # Attendance of Individual Student saved on AttendanceReport Model 
            student = Students.objects.get(admin=stud['id']) 
  
            attendance_report = AttendanceReport.objects.get(student_id=student, 
                                                             attendance_id=attendance) 
            attendance_report.status=stud['status'] 
  
            attendance_report.save() 
        return HttpResponse("OK") 
    except: 
        return HttpResponse("Error") 
  