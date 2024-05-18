
from django.urls import path
from . import views

urlpatterns = [
   
    path('home/',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
   # path('result/',views.result,name='result'),
    path('upload/',views.upload,name='upload'),
    path('404/',views.error,name='error')
]
