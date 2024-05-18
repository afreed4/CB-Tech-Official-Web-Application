from django.shortcuts import render,redirect
from .models import Activity,Event,SportsAndArts,Venue
from .forms import EventForm,ActivityForm,SportAndArtsForm,VenuForm
# Create your views here.

def activity_view(request):
  
    if request.POST:
        event=request.POST.get('event')
        title=request.POST.get('title')
        slug=request.POST.get('slug')
        discription=request.POST.get('discription')
        form=Activity(name=title, activity=event, slug=slug, discription=discription)
        
        form.save()
        
        if event=='Event':
            return redirect('event')
        elif event=='Class':
            return redirect('sports_and_arts')
        elif event=='Venue':
            return redirect('sports_and_arts') 
    else:
        form=ActivityForm()
        return render(request,'activity.html',{'form':form})


def event_view(request):
    if request.POST:
        form=EventForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity')
    else:
        form=EventForm()
        return render(request,'event.html',{'form':form})
    
    
def sport_view(request):
     if request.POST:
        form=SportAndArtsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity')
        else:
         form=SportAndArtsForm()
         return render(request,'sports_and_arts.html',{'form':form})

def venue_view(request):
    if request.POST:
        form=VenuForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activity')
        else:
         form=VenuForm()
         return render(request,'venue.html',{'form':form})

def base_view(request):
    return render(request,'base.html')
            

        
        