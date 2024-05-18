from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('edit/',views.edit,name='edit'),
    path('list/',views.list,name='list'),
    path('photo/',views.photos,name='photo_upload'),
    path('photo_display/',views.photo_display,name='photo_display'),
    path('success/',views.success,name='success')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)