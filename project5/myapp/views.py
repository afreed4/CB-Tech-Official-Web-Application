from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect,Http404,JsonResponse,FileResponse,HttpResponse,StreamingHttpResponse
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def register_view(request):
    
    if request.POST:
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        passwrod1=request.POST['pass1']
        passwrod2=request.POST['pass2']
        
        if passwrod1 != passwrod2:
            messages.error(request,'Password is not match')
            return redirect('register')
        
        user=User.objects.create_user(username, email, passwrod1)
        redirect_url=reverse('add_blog')
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        return render(request,'login.html',{'redirect_url':redirect_url})
     
    else:
        
        return render(request,'registr.html')

def login_view(request):
    
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        
        if user is not None:
           login(request,user)
           messages.success(request,"SuccessFuly Logged In")
           return render(request,'profile.html')
        else:
           messages.error(request,"The Password Or The Username Is Incorrect Please Try Again")
        return redirect('profile/<int:id>')
    
    return render(request,'login.html')

def Profile_view(request,id):
     if request.POST:
         result=Profile_DB.objects.get(id=id)
         return redirect('profile',{'result':result})
     else:
        
         return render(request,'profile.html',)

def edit_view(request):
 try:
        profile=request.user.profile_db
 except Profile_DB.DoesNotExist:
        profile=Profile_DB(user=request.user)
 
 if request.POST:
        
        print("i am at requesting post")
        form=Profile(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            print("form is valid")
            form.save()
            print("saved")
            alert=True
            print("alerted")
            return render(request,'profile.html',{'form':form, 'alert':alert})
        else:
            print("not valid")
 else:
      print("its in else ")
     
      form=Profile(instance=profile)
      return render(request,'edit.html',{'form':form})

def home_view(request):
    posts=Blogpost_DB.objects.all()
    posts2=Blogpost_DB.objects.filter().order_by('-dateTime')
    return render(request,'home.html',{'posts':posts, 'posts2':posts2})

def add_blog(request):
    if request.method=='POST':
        print("req is at post")
        form=BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print("form validated")
            blogpost=form.save(commit=False)
            blogpost.author=request.user
            blogpost.save()
            print("blog post saved")
            obj=form.instance
            alert=True
            return redirect('home')
    else:
        print("again else ")
        form=BlogPostForm()
        return render(request,'add_blogs.html',{'form':form})
           

def logout_view(request):
    if request.POST:
        print("request is post")
        logout(request)
        print("logg out completed")
        return redirect('register')
    else:
        print("somthing went wrong")
        return render(request,'profile.html')

def base_view(request):
    return render(request,'base.html')

def blog_comment(request,slug):
    post=Blogpost_DB.objects.filter(slug=slug).first()
    comments=Comment_DB.objects.filter(blog=post)
    if request.POST:
        user=request.user 
        content=request.POST.get('content','')
        blog_id=request.POST.get('blog_id','')
        comment=Comment_DB(user=user, content=content, blog=post)
        comment.save()
        return redirect('blog_comment',slug=slug)
    
    else:
        
        return render(request,'blog_comment.html',{'post':post, 'comments':comments})
