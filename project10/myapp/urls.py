
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home_view,name='name'),
    
    path('counsillor_regsiter/',views.Counsillor_sighnup_view,name='counsillor_regsiter'),
    path('counsillor_login/',views.Counsillor_login_view,name='counsillor_login'),
    path('counsillor_home/',views.counsillor_home,name='counsillor_home'),
    
    path('faculty_register/',views.Faculy_sighnup_view,name='faculty_register'),
    path('faculty_login/',views.Faculty_login_view,name='faculty_login'),
    path('faculty_home/',views.faculty_home,name='faculty_home'),
    
    path('add_student/',views.add_student_view,name='add_student'),
    
    path('attendance/',views.attendence_view,name='attendance'),
    
    path('attendance_report/<int:id>/',views.attendence_report_view,name='attendance_report')
    
]
