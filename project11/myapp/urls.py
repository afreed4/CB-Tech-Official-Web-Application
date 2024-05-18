
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base_view,name='base'),
    path('activity/',views.activity_view,name='activity'),
    path('event/',views.event_view,name='event'),
    path('sports_and_arts/',views.sport_view,name='sports_and_arts')
]