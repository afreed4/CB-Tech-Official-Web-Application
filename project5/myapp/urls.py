
from django.urls import path
from .import views
urlpatterns = [
    path('base/',views.base_view,name='base'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register'),
    path('',views.home_view,name='home'),
    path('edit/',views.edit_view,name='edit'),
    path('profile/<int:id>/',views.Profile_view,name='profile'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('blog_comment/<str:slug>/',views.blog_comment,name='blog_comment'),
]
