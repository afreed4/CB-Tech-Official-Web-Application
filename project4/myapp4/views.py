from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from . models import employi_db
from . forms import EmployeeForm
# Create your views here.

def list_view(request):
    recent_visit=request.session.get('recent_visit',[])
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count
    recent_data=employi_db.objects.filter(pk__in=recent_visit)
    context=employi_db.objects.all()
    
    return render(request,'employee/list.html',{'context':context,'recent_data':recent_data, 'count':count})

def create_view(request):
    
    if request.POST:
        form=EmployeeForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('list')
    else:
        form=EmployeeForm()
        cntext={
            'form':form,
        }
        return render(request,'employee/create.html',cntext)

def delete_view(request, pk):
    employee=employi_db.objects.get(id=pk)
    if request.POST:
        employee.delete()
        return redirect('list')
            
    return render(request,'employee/delete.html')

def edit_view(request, pk):
    employee=employi_db.objects.get(id=pk)
    form=EmployeeForm(instance=employee)
    if request.POST:
       form=EmployeeForm(request.POST, instance=employee)
       if form.is_valid():
           form.save()
           return redirect('list')
    else:
        recent_visit=request.session.get('recent_visit',[])
        recent_visit.insert(0,pk)
        request.session['recent_visit']=recent_visit
        context={
        'employee':employee,
        'form':form
        }
    return render(request,'employee/edit.html',context)

def base_view(request):
    
    return render(request,'base.html')