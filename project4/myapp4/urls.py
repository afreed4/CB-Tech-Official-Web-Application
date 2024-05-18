from django.urls import path
from . import views 
urlpatterns = [
    path('',views.list_view,name='list'),
    path('create/',views.create_view,name='create'),
    path('edit/<str:pk>/',views.edit_view,name='edit'),
    path('delete/<str:pk>/',views.delete_view,name='delete'),
    path('home/',views.base_view,name='Home'),
]