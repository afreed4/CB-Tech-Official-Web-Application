from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import accountantform
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.contrib.auth import get_user_model

from cbtech_app.models import CustomUser,  Courses, Enquiry

User = get_user_model()
current_date = datetime.now()
previous_month = current_date - relativedelta(months=1)
timezone.now().date()


def filter_by_status(status_of_enquiry):
    registered = Enquiry.objects.filter(status_of_enquiry = status_of_enquiry).order_by('-enquiry_id')
    return registered

def filter_by_lead(lead_type):
    leads = Enquiry.objects.filter(lead_type = lead_type)
    return leads


def manage_enquiry(request):
    students = Enquiry.objects.filter(status_of_enquiry='Registered').order_by('-enquiry_id')
    context = {
        "Enquiries": students
    }
    return render(request,"accountant-templates/manage_enquiry.html",context)

@login_required(login_url='/')
def accountant_edit_enquiry(request, enquiry_id):
    # Adding Student ID into Session Variable

    enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
    form = accountantform(instance=enquiry,initial={'amount': 0})
    context = {
        "id": enquiry.enquiry_id,
        'reg_id':enquiry.student_registration_id,
        "form": form
    }
    return render(request, "accountant-templates/edit_enquiry.html", context)

@login_required(login_url='/')
def accountant_edit_enquiry_save(request,enquiry_id):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        enquiry = Enquiry.objects.get(enquiry_id=enquiry_id)
        form = accountantform(request.POST,instance = enquiry,initial={'amount': 0})
        amount_payed=int(request.POST["amount"])
        pay_date=request.POST["payment_date"]
        amount=amount_payed+int(enquiry.total_amount_paid)

        if form.is_valid():           
            form.save()
            enquiry.total_amount_paid=amount
            if(amount_payed>0):
                pay_date=str(pay_date)
                amount_payed=str(amount_payed)              
                enquiry.payment_History=str(enquiry.payment_History)+ "\n"+"  "+pay_date+"  "+amount_payed+"Rs/-"
                
            enquiry.save()
            return redirect('accountant_manage')
        else:
            messages.error(request,'Check the details and try again!')
            context = {
            "id": enquiry_id,
            "form": form,
            }
            return render(request, "accountant-templates/edit_enquiry.html", context)
