from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage

from . models import Datas
from . models import Photo
from . forms import PhotoForm
from django.views.generic import TemplateView
# Create your views here.



def create(request):
 
   if request.POST:
      name=request.POST.get('name')
      number=request.POST.get('number')
      club=request.POST.get('club')      
      
      data_obj=Datas(Name=name, Number=number, Club=club)
      data_obj.save()
      
   
   return render(request,'create.html')

def edit(request):
    pictures={
        'img':'maradona.jpg',
        'img':'messi-iphone-fhku23h1ap4e31ql.jpg',
        'img':'Maldini_Wallpaper.jpeg',
        'img':'wp2298707-gennaro-gattuso-wallpapers.jpg'
    }
    return render(request,'edit.html',pictures)

def list(request):
   players_data=Datas.objects.all()
   
   return render(request,'list.html',{'players_data':players_data})

def photos(request):
    if request.POST:
        form=PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=PhotoForm()
        return render(request,'photo.html',{'form':form})

def photo_display(request):
    result=Photo.objects.all()
    paginator=Paginator(result,10)
    page=request.GET.get('page')
    
    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items=paginator.page(1)
    except EmptyPage:
        items=paginator.page(paginator.num_pages)
        
    return render(request,'photo_display.html',{'items':items})

def success(request):
    picture={
        'img':'1930264_check_complete_done_green_success_icon.png'
    }
    return render(request,'success.html',picture)