from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import SighnupForm,LoginForm


# Create your views here.

def home(request):
    return render(request,'home.html')
def login1(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                return render(request,'login.html',{'form':form,'error':'invalid credntials'})
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def logout1(request):
    if request.method=='POST':
        logout(request)
        
      
        
        return redirect('logout')
    else:
        print('goes to error')
        return render(request,'error.html')

def sighnup(request):
    if request.POST:
        form=SighnupForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('first_ac')
    else:
        form=SighnupForm()
    return render(request,'sighnup.html',{'form':form})    
        
def login_profile(request):
    return render(request,'profile.html')

def sighnup_profile(request):
    return render(request,'new.html')

def first_ac(request):
    return render(request,'first_ac.html')

def logout_view(request):
    return render(request,'logout.html')

def base_view(request):
    return render(request,'base.html')