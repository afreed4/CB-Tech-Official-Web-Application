from typing import Any
from django.http import  HttpRequest, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Albums,AlbumDetailView
from . forms import PhotoForm
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
# Create your views here.

def menu(request):
    return render(request,'menu.html')

def home(request):
    return render(request,'home.html')

def upload(request):
    list=Albums.objects.filter(visible=True).order_by('-create')
    paginator=Paginator(list,10) # Show 25 contacts per page.
    page=request.GET.get('page')
    
    try:
        albums=paginator.page(page)
    except PageNotAnInteger:
        albums=paginator.page(1)
    except EmptyPage:
        albums=paginator.page(paginator.num_pages)
        
    return render(request,'upload.html',{'albums':list})

class AlbumDetail(DetailView):
    model=Albums
    def get_context_data(self, **kwargs):
        context= super(AlbumDetail,self).get_context_data(**kwargs)
        context['images']=AlbumDetailView.objects.filter(album=self.object.id)
        return (context)

def error(request, exception):
    assert isinstance(request,HttpRequest)
    return render(request,'404.html',None,None,404)
