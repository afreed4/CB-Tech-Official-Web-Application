from django.urls import path
from . import views,staffviews

urlpatterns = [
    path('admin_home/', views.admin_home, name="admin_home"),
    path('staff_home/', staffviews.staff_home, name="staff_home"), 
    path('staff_take_attendance/', staffviews.staff_take_attendance, name="staff_take_attendance"), 
    path('get_students/', staffviews.get_students, name="get_students"), 
    path('save_attendance_data/', staffviews.save_attendance_data, name="save_attendance_data"), 
    path('get_attendance_dates/', staffviews.get_attendance_dates, name="get_attendance_dates"), 
    path('get_attendance_student/', staffviews.get_attendance_student, name="get_attendance_student"), 
    path('update_attendance_data/', staffviews.update_attendance_data, name="update_attendance_data"), 
    path('registration', views.registration, name="registration"), 
    path('login', views.loginUser, name="login"), 
    path('doLogin', views.doLogin, name="doLogin"), 
    path('doRegistration', views.doRegistration, name="doRegistration"), 
      
]