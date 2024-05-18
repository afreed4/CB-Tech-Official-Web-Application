from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('',views.form2_view,name='forms'),
    path('base/',views.base_view,name='base'),
    path('course/',views.course_view,name='course'),
    path('repeated_user/',views.repeated_user_view,name='repeated_user'),
    path('register',views.Registerationform,name='StudentRegistration'),
    path('fetch/',views.get_data,name='fetch')
]
