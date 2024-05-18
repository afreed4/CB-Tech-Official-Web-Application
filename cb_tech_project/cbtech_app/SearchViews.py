from django.shortcuts import render,redirect
from cbtech_app.models import *
from django.db.models import Q
import re
from datetime import datetime

# Create your views here.


def searchEnquiry(request):
    if 'q' in request.GET:
        query = request.GET.get('q')

        if query:
                keywords = [keyword.strip().lower() for keyword in query.split(',')]
                
                q_objects = Q()
                for keyword in keywords:
                    date_obj = None

                    print(keyword)
                    clean_query = re.sub(r'\W+', '', keyword).lower()
                    try:
                        year_number = datetime.strptime(clean_query, '%Y').year                 # example:'year'
                        date_obj = [
                                            datetime(day=1, month=1, year=year_number),
                                            datetime(day=31, month=12, year=year_number)
                                        ]
                    except ValueError:
                        try:
                            month_number = datetime.strptime(clean_query, '%m%Y').month         # example:'month(int)-year'
                            year_number = datetime.strptime(clean_query, '%m%Y').year
                            date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                        except ValueError:
                            try:
                                month_number = datetime.strptime(clean_query, '%b%Y').month     # example:'month(short)-year'
                                year_number = datetime.strptime(clean_query, '%b%Y').year
                                date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                            except ValueError:
                                try:
                                    month_number = datetime.strptime(clean_query, '%B%Y').month     # example:'month(full)-year'
                                    year_number = datetime.strptime(clean_query, '%B%Y').year
                                    date_obj = [
                                        datetime(day=1, month=month_number, year=year_number),
                                        datetime(day=31, month=month_number, year=year_number)
                                    ]
                                except ValueError:
                                    try:
                                        month_number = datetime.strptime(clean_query, '%b').month       # example:'month(short)'
                                        current_year = datetime.now().year
                                        date_obj = [
                                            datetime(day=1, month=month_number, year=current_year),
                                            datetime(day=31, month=month_number, year=current_year)
                                        ]
                                    except ValueError:
                                        try:
                                            month_number = datetime.strptime(clean_query, '%B').month       # example:'month(full)'
                                            current_year = datetime.now().year
                                            date_obj = [
                                                datetime(day=1, month=month_number, year=current_year),
                                                datetime(day=31, month=month_number, year=current_year)
                                            ]
                                        except ValueError:
                                            date_obj = None
                    try:
                    #     pdate = datetime.strptime(clean_query, '%d').date       # example:'date(int)'
                    #     current_year = datetime.now().year
                    #     month_number  = datetime.now().month
                    #     date_obj = datetime(day=pdate, month=month_number, year=current_year)
                    # except ValueError:
                    #     try:
                        date_obj = datetime.strptime(clean_query, '%d%m')       # example:'date(int)-month(num)'
                        date_obj = date_obj.replace(year=datetime.now().year)
                    except ValueError:
                        try:
                                date_obj = datetime.strptime(clean_query, '%d%b')       # example:'date(int)-month(short)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                        except ValueError:
                            try:
                                date_obj = datetime.strptime(clean_query, '%d%B')       # example:'date(int)-month(full)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                            except ValueError:
                                try:
                                        date_obj = datetime.strptime(clean_query, '%d%m%Y')     # example:'date(int)-month(int)-year'
                                except ValueError:
                                    try:
                                        date_obj = datetime.strptime(clean_query, '%d%b%Y')     # example:'date(int)-month(short)-year'
                                    except ValueError:
                                        try:
                                            date_obj = datetime.strptime(clean_query, '%d%B%Y')     # example:'date(int)-month(full)-year'
                                        except ValueError:
                                            if date_obj:
                                                pass
                                            else:
                                                date_obj = None        


                    if date_obj:
                        if type(date_obj)==list:
                            q_objects &= Q(date_of_enquiry__range=(date_obj[0], date_obj[1]))
                        else:
                            q_objects &= Q(date_of_enquiry__day=date_obj.day, date_of_enquiry__month=date_obj.month, date_of_enquiry__year=date_obj.year)
                    else:        
                        q_objects &= (Q(name__icontains=keyword) |
                                Q(phone_number__icontains=keyword) |
                                Q(email_id__icontains=keyword) |
                                Q(gender__icontains=keyword) |
                                Q(qualification__icontains=keyword) |
                                Q(technical_skills__icontains=keyword) |
                                Q(lead_type__icontains=keyword) |
                                Q(status_of_enquiry__startswith=keyword)|
                                Q(consultant_name__icontains=keyword) |
                                Q(course_completion__icontains=keyword)
                                )
                    print(q_objects)
                    search_results = Enquiry.objects.filter(q_objects)
                    search_results2 = Enquiry.objects.filter(Q(course_completion__gt=20) & Q(course_completion__lt=80) & q_objects)
                    complete_search=search_results+search_results2
                    print(search_results2)
        else:
            print("search in else ")
            return redirect('manage_enquiry')
        return render(request, "admin_template/manage_enquiry_template.html", {'query':query,'complete_search': complete_search})

def staffsearchEnquiry(request):
    if 'q' in request.GET:
        query = request.GET.get('q')

        if query:
                keywords = [keyword.strip().lower() for keyword in query.split(',')]
                
                q_objects = Q()
                for keyword in keywords:
                    date_obj = None
                
                    clean_query = re.sub(r'\W+', '', keyword).lower()
                    try:
                        year_number = datetime.strptime(clean_query, '%Y').year                 # example:'year'
                        date_obj = [
                                            datetime(day=1, month=1, year=year_number),
                                            datetime(day=31, month=12, year=year_number)
                                        ]
                    except ValueError:
                        try:
                            month_number = datetime.strptime(clean_query, '%m%Y').month         # example:'month(int)-year'
                            year_number = datetime.strptime(clean_query, '%m%Y').year
                            date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                        except ValueError:
                            try:
                                month_number = datetime.strptime(clean_query, '%b%Y').month     # example:'month(short)-year'
                                year_number = datetime.strptime(clean_query, '%b%Y').year
                                date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                            except ValueError:
                                try:
                                    month_number = datetime.strptime(clean_query, '%B%Y').month     # example:'month(full)-year'
                                    year_number = datetime.strptime(clean_query, '%B%Y').year
                                    date_obj = [
                                        datetime(day=1, month=month_number, year=year_number),
                                        datetime(day=31, month=month_number, year=year_number)
                                    ]
                                except ValueError:
                                    try:
                                        month_number = datetime.strptime(clean_query, '%b').month       # example:'month(short)'
                                        current_year = datetime.now().year
                                        date_obj = [
                                            datetime(day=1, month=month_number, year=current_year),
                                            datetime(day=31, month=month_number, year=current_year)
                                        ]
                                    except ValueError:
                                        try:
                                            month_number = datetime.strptime(clean_query, '%B').month       # example:'month(full)'
                                            current_year = datetime.now().year
                                            date_obj = [
                                                datetime(day=1, month=month_number, year=current_year),
                                                datetime(day=31, month=month_number, year=current_year)
                                            ]
                                        except ValueError:
                                            date_obj = None
                    try:
                    #     pdate = datetime.strptime(clean_query, '%d').date       # example:'date(int)'
                    #     current_year = datetime.now().year
                    #     month_number  = datetime.now().month
                    #     date_obj = datetime(day=pdate, month=month_number, year=current_year)
                    # except ValueError:
                    #     try:
                        date_obj = datetime.strptime(clean_query, '%d%m')       # example:'date(int)-month(num)'
                        date_obj = date_obj.replace(year=datetime.now().year)
                    except ValueError:
                        try:
                                date_obj = datetime.strptime(clean_query, '%d%b')       # example:'date(int)-month(short)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                        except ValueError:
                            try:
                                date_obj = datetime.strptime(clean_query, '%d%B')       # example:'date(int)-month(full)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                            except ValueError:
                                try:
                                        date_obj = datetime.strptime(clean_query, '%d%m%Y')     # example:'date(int)-month(int)-year'
                                except ValueError:
                                    try:
                                        date_obj = datetime.strptime(clean_query, '%d%b%Y')     # example:'date(int)-month(short)-year'
                                    except ValueError:
                                        try:
                                            date_obj = datetime.strptime(clean_query, '%d%B%Y')     # example:'date(int)-month(full)-year'
                                        except ValueError:
                                            if date_obj:
                                                pass
                                            else:
                                                date_obj = None        
                                                
                    if date_obj:
                        if type(date_obj)==list:
                            q_objects &= Q(date_of_enquiry__range=(date_obj[0], date_obj[1]))
                        else:
                            q_objects &= Q(date_of_enquiry__day=date_obj.day, date_of_enquiry__month=date_obj.month, date_of_enquiry__year=date_obj.year)
                    else:        
                        q_objects &= (Q(name__icontains=keyword) |
                                Q(phone_number__icontains=keyword) |
                                Q(email_id__icontains=keyword) |
                                Q(gender__icontains=keyword) |
                                Q(qualification__icontains=keyword) |
                                Q(technical_skills__icontains=keyword) |
                                Q(lead_type__icontains=keyword) |
                                Q(status_of_enquiry__startswith=keyword)|
                                Q(consultant_name__icontains=keyword) 
                                )
                    search_results = Enquiry.objects.filter(q_objects)
        else:
            return redirect('staff_manage_enquiry')
        return render(request, "staff_template/staff_manage_enquiry.html", {'query':query,'searchEnquiry': search_results})





def filter_by_status(status_of_enquiry):
    registered = Enquiry.objects.filter(status_of_enquiry = status_of_enquiry)
    return registered


def searchRegisteration(request):
    if 'q' in request.GET:
        query = request.GET.get('q')

        if query:
                keywords = [keyword.strip().lower() for keyword in query.split(',')]
                
                q_objects = Q()
                object1 = filter_by_status("Registered")
                for keyword in keywords:
                    date_obj = None
                
                    clean_query = re.sub(r'\W+', '', keyword).lower()
                    try:
                        year_number = datetime.strptime(clean_query, '%Y').year                 # example:'year'
                        date_obj = [
                                            datetime(day=1, month=1, year=year_number),
                                            datetime(day=31, month=12, year=year_number)
                                        ]
                    except ValueError:
                        try:
                            month_number = datetime.strptime(clean_query, '%m%Y').month         # example:'month(int)-year'
                            year_number = datetime.strptime(clean_query, '%m%Y').year
                            date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                        except ValueError:
                            try:
                                month_number = datetime.strptime(clean_query, '%b%Y').month     # example:'month(short)-year'
                                year_number = datetime.strptime(clean_query, '%b%Y').year
                                date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                            except ValueError:
                                try:
                                    month_number = datetime.strptime(clean_query, '%B%Y').month     # example:'month(full)-year'
                                    year_number = datetime.strptime(clean_query, '%B%Y').year
                                    date_obj = [
                                        datetime(day=1, month=month_number, year=year_number),
                                        datetime(day=31, month=month_number, year=year_number)
                                    ]
                                except ValueError:
                                    try:
                                        month_number = datetime.strptime(clean_query, '%b').month       # example:'month(short)'
                                        current_year = datetime.now().year
                                        date_obj = [
                                            datetime(day=1, month=month_number, year=current_year),
                                            datetime(day=31, month=month_number, year=current_year)
                                        ]
                                    except ValueError:
                                        try:
                                            month_number = datetime.strptime(clean_query, '%B').month       # example:'month(full)'
                                            current_year = datetime.now().year
                                            date_obj = [
                                                datetime(day=1, month=month_number, year=current_year),
                                                datetime(day=31, month=month_number, year=current_year)
                                            ]
                                        except ValueError:
                                            date_obj = None
                    try:
                    #     pdate = datetime.strptime(clean_query, '%d').date       # example:'date(int)'
                    #     current_year = datetime.now().year
                    #     month_number  = datetime.now().month
                    #     date_obj = datetime(day=pdate, month=month_number, year=current_year)
                    # except ValueError:
                    #     try:
                        date_obj = datetime.strptime(clean_query, '%d%m')       # example:'date(int)-month(num)'
                        date_obj = date_obj.replace(year=datetime.now().year)
                    except ValueError:
                        try:
                                date_obj = datetime.strptime(clean_query, '%d%b')       # example:'date(int)-month(short)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                        except ValueError:
                            try:
                                date_obj = datetime.strptime(clean_query, '%d%B')       # example:'date(int)-month(full)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                            except ValueError:
                                try:
                                        date_obj = datetime.strptime(clean_query, '%d%m%Y')     # example:'date(int)-month(int)-year'
                                except ValueError:
                                    try:
                                        date_obj = datetime.strptime(clean_query, '%d%b%Y')     # example:'date(int)-month(short)-year'
                                    except ValueError:
                                        try:
                                            date_obj = datetime.strptime(clean_query, '%d%B%Y')     # example:'date(int)-month(full)-year'
                                        except ValueError:
                                            if date_obj:
                                                pass
                                            else:
                                                date_obj = None        
                    if date_obj:
                        if type(date_obj)==list:
                            q_objects &= Q(date_of_registration__range=(date_obj[0], date_obj[1]))
                        else:
                            q_objects &= Q(date_of_registration__day=date_obj.day, date_of_registration__month=date_obj.month, date_of_registration__year=date_obj.year)
                    else:        
                        q_objects &= (Q(student_registration_id__icontains=keyword)|Q(name__icontains=keyword) |
                                Q(phone_number__icontains=keyword) |
                                Q(email_id__icontains=keyword) |
                                Q(gender__icontains=keyword) |
                                Q(qualification__icontains=keyword) |
                                Q(technical_skills__icontains=keyword) |
                                Q(lead_type__icontains=keyword) |
                                Q(consultant_name__icontains=keyword) 
                                )
                    search_results = object1.filter(q_objects)
        else:
            return redirect('manage_registeration')
        return render(request,"admin_template/manage_registeration_template.html", {'query':query,'searchRegister': search_results})


def searchRegisterationAccountant(request):
    if 'q' in request.GET:
        query = request.GET.get('q')

        if query:
                keywords = [keyword.strip().lower() for keyword in query.split(',')]
                
                q_objects = Q()
                object1 = filter_by_status("Registered")
                for keyword in keywords:
                    date_obj = None
                
                    clean_query = re.sub(r'\W+', '', keyword).lower()
                    try:
                        year_number = datetime.strptime(clean_query, '%Y').year                 # example:'year'
                        date_obj = [
                                            datetime(day=1, month=1, year=year_number),
                                            datetime(day=31, month=12, year=year_number)
                                        ]
                    except ValueError:
                        try:
                            month_number = datetime.strptime(clean_query, '%m%Y').month         # example:'month(int)-year'
                            year_number = datetime.strptime(clean_query, '%m%Y').year
                            date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                        except ValueError:
                            try:
                                month_number = datetime.strptime(clean_query, '%b%Y').month     # example:'month(short)-year'
                                year_number = datetime.strptime(clean_query, '%b%Y').year
                                date_obj = [
                                            datetime(day=1, month=month_number, year=year_number),
                                            datetime(day=31, month=month_number, year=year_number)
                                        ]
                            except ValueError:
                                try:
                                    month_number = datetime.strptime(clean_query, '%B%Y').month     # example:'month(full)-year'
                                    year_number = datetime.strptime(clean_query, '%B%Y').year
                                    date_obj = [
                                        datetime(day=1, month=month_number, year=year_number),
                                        datetime(day=31, month=month_number, year=year_number)
                                    ]
                                except ValueError:
                                    try:
                                        month_number = datetime.strptime(clean_query, '%b').month       # example:'month(short)'
                                        current_year = datetime.now().year
                                        date_obj = [
                                            datetime(day=1, month=month_number, year=current_year),
                                            datetime(day=31, month=month_number, year=current_year)
                                        ]
                                    except ValueError:
                                        try:
                                            month_number = datetime.strptime(clean_query, '%B').month       # example:'month(full)'
                                            current_year = datetime.now().year
                                            date_obj = [
                                                datetime(day=1, month=month_number, year=current_year),
                                                datetime(day=31, month=month_number, year=current_year)
                                            ]
                                        except ValueError:
                                            date_obj = None
                    try:
                    #     pdate = datetime.strptime(clean_query, '%d').date       # example:'date(int)'
                    #     current_year = datetime.now().year
                    #     month_number  = datetime.now().month
                    #     date_obj = datetime(day=pdate, month=month_number, year=current_year)
                    # except ValueError:
                    #     try:
                        date_obj = datetime.strptime(clean_query, '%d%m')       # example:'date(int)-month(num)'
                        date_obj = date_obj.replace(year=datetime.now().year)
                    except ValueError:
                        try:
                                date_obj = datetime.strptime(clean_query, '%d%b')       # example:'date(int)-month(short)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                        except ValueError:
                            try:
                                date_obj = datetime.strptime(clean_query, '%d%B')       # example:'date(int)-month(full)'
                                date_obj = date_obj.replace(year=datetime.now().year)
                            except ValueError:
                                try:
                                        date_obj = datetime.strptime(clean_query, '%d%m%Y')     # example:'date(int)-month(int)-year'
                                except ValueError:
                                    try:
                                        date_obj = datetime.strptime(clean_query, '%d%b%Y')     # example:'date(int)-month(short)-year'
                                    except ValueError:
                                        try:
                                            date_obj = datetime.strptime(clean_query, '%d%B%Y')     # example:'date(int)-month(full)-year'
                                        except ValueError:
                                            if date_obj:
                                                pass
                                            else:
                                                date_obj = None        
                                                
                    if date_obj:
                        if type(date_obj)==list:
                            q_objects &= Q(date_of_registration__range=(date_obj[0], date_obj[1]))
                        else:
                            q_objects &= Q(date_of_registration__day=date_obj.day, date_of_registration__month=date_obj.month, date_of_registration__year=date_obj.year)
                    else:        
                        q_objects &= (Q(name__icontains=keyword) |
                                Q(phone_number__icontains=keyword) |
                                Q(email_id__icontains=keyword) |
                                Q(gender__icontains=keyword) |
                                Q(qualification__icontains=keyword) |
                                Q(technical_skills__icontains=keyword) |
                                Q(lead_type__icontains=keyword) |
                                Q(consultant_name__icontains=keyword) |
                                Q(student_registration_id__icontains=keyword) 
                                )
                    print(q_objects)
                    search_results = object1.filter(q_objects)
        else:
            return redirect('accountant_manage')
        return render(request,"accountant-templates/manage_enquiry.html", {'query':query,'searchRegister': search_results})

