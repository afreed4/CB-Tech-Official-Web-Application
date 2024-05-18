
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login1,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout_view,name='logout'),
    path('sighnup/',views.sighnup,name='sighnup'),
    path('profile/',views.login_profile,name='profile'),
    path('new/',views.sighnup_profile,name='sighnup_profile'),
    path('first_ac/',views.first_ac,name='first_ac'),
    path('base/',views.base_view,name='base'),
]