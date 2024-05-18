from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('attendance_submit/', views.attendance_submit, name='Master-attendance_submit'),
    path('view/', views.view_attendance, name='Master-view'),
   # path('view/', views.view_attendance, name='Master-view'),
]