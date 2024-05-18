from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.utils import timezone
import random
from calendar import monthrange
import datetime
import re

today = datetime.date.today()

current_year = today.year

def extract_numeric_part(input_str):
    if input_str is None:
        return 0
    match = re.search(r'(\d{4})', input_str)
    if match:
        return match.group(1)
    else:
        return 0



def get_random_date_next_month():
    
    current_datetime = timezone.now()

    
    next_month = current_datetime.month + 1 if current_datetime.month < 12 else 1
    next_month_year = current_datetime.year + 1 if current_datetime.month == 12 else current_datetime.year
    first_day_next_month = timezone.datetime(next_month_year, next_month, 1, tzinfo=current_datetime.tzinfo)
    
    last_day_next_month = first_day_next_month.replace(day=monthrange(next_month_year, next_month)[1])
    
    random_datetime = timezone.make_aware(timezone.datetime.fromtimestamp(random.randint(int(first_day_next_month.timestamp()), int(last_day_next_month.timestamp()))))

    return random_datetime


class CustomUser(AbstractUser):
    STAFF_TYPES = (
        ('Admin', 'Administrator'),
        ('Faculty', 'Faculty'),
        ('Counsellor', 'Counsellor'),
        ('Accountant', 'Accountant'),
        ('Manager','Marketing Manager')
    )   
    staff_type = models.CharField(max_length=12, choices=STAFF_TYPES)
    contact_number = models.CharField(max_length=15)

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    type_choices = (
        ('Full Time','Full Time'),
        ('Crash','Crash'),
        ('Project','Project'),
    )
    course_type = models.CharField(max_length=10,choices=type_choices,blank=True,null=True)
    course_duration = models.CharField(max_length=25,default='4 Months',choices=type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    joined_date=models.DateField(blank=True,null=True,auto_now_add=True)
    
    def __str__(self):
	    return self.course_name


class Enquiry(models.Model):
    #Personal details
    name=models.CharField(max_length=40, blank=False,)
    phone_number=models.CharField(max_length=15)
    email_id=models.CharField(max_length=60)
    gender = models.CharField(max_length=8,blank=True,null=True)
    guardian_name=models.CharField(max_length=40, blank=True,null=True)
    alternate_phone_number=models.CharField(blank=True,null=True,max_length=15)
    address=models.TextField(max_length=80, blank=True,null=True)
    
    #educational details
    college=models.CharField(max_length=30,blank=True,null=True)
    qualification = models.CharField(max_length=30,blank=False,null=True)
    year_of_pass =models.IntegerField(null=False,blank=False,default=current_year)
    technical_skills=models.CharField(max_length=60,blank=True,null=True)
    
    #enquiry details
    enquiry_id= models.AutoField(primary_key=True)
    lead_type=models.CharField(max_length=30,blank=True,null=True,default='Walk-In')
    status_of_enquiry = models.CharField(max_length=15,default='Not Contacted',blank=True,null=True)
    date_of_enquiry=models.DateField(default=timezone.now)
    remarks=models.TextField(max_length=120,blank=True,null=True)
    
    #registeration details
    mode_of_class = models.CharField(max_length=10,blank=True,null=True)
    student_registration_id = models.CharField(max_length=40,blank=True,null=True,default=None)
    date_of_registration=models.DateField(blank=False,null=True,default=timezone.now)
    profile_pic=models.ImageField(upload_to = 'photos/', blank=True,null=True)
    
    #course details
    course = models.CharField(max_length=20,blank=True,null=True)
    type_choices = (
        ('Full Time','Full Time'),
        ('Crash','Crash'),
        ('Project','Project'),
    )
    course_type = models.CharField(max_length=10,choices=type_choices,blank=True,null=True)
    course_duration = models.CharField(max_length=25,default='4 Months',choices=type_choices)
    #created_at = models.DateTimeField(auto_now_add=True)
    #course_type = models.CharField(max_length=10,null=True,blank=False)
    joined_date=models.DateField(blank=True,null=True,auto_now_add=True)
    course_status = models.CharField(max_length=10,blank=True,null=True)
    
    
    #payment details
    total_amount=models.PositiveIntegerField(blank=True,default=0000)
    number_of_installments = models.IntegerField(default=0)
    next_due_date = models.DateField(default=get_random_date_next_month())
    payment_status = models.CharField(max_length=15,blank=True,null=True)
    payment_History = models.TextField(blank=True,default="",null=True)
    payment_method = models.CharField(max_length=20,blank=True,null=True)
    # amount_paid = models.PositiveIntegerField(blank=True,null=True,default=000)
    # outstanding_amount = models.PositiveIntegerField(blank=True,null=True,default=000)
    amount= models.PositiveIntegerField(null=False,default=000)
    total_amount_paid = models.PositiveIntegerField(null=False,default=000)
    outstanding_amount = models.PositiveIntegerField(null=False,default=000)
    payment_receipt_number = models.CharField(max_length=20,blank=True,null=True)
    payment_date = models.DateField(blank=True,null=True)

    #other details
    declaration_type = models.CharField(max_length=10,null=True,blank=False)
    declaration = models.CharField(max_length=10,null=True,blank=False)
    consultant_name = models.CharField(max_length=10,blank=False,null=False,default='')
    faculty_name = models.CharField(max_length=20,blank=True,null=True)
    reference_name = models.CharField(max_length=40,blank=True,null=True)
    reference_contact_number = models.CharField(blank=True,null=True,default='',max_length=15)
    marketing_manager=models.CharField(max_length=40,null=True,blank=True)
    office = models.CharField(max_length=13,blank=True,null=True)
    updated_by = models.CharField(max_length=40,null=True,blank=False)
    updated_date = models.DateField(null=True,blank=False)
    
    #course status
    project_status = models.CharField(null=True,max_length=15,blank=True)
    certificate = models.CharField(null=True,max_length=55,blank=True)
    exam = models.CharField(null=True,max_length=15,blank=True)
    course_completion=models.CharField(null=True,max_length=100,blank=True)
    placement_session_attended=models.CharField(null=True,max_length=200,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.outstanding_amount = self.total_amount - self.total_amount_paid
        
        super(Enquiry, self).save(*args, **kwargs)

    @property
    def registration_id(self):
        prefix=''
        if self.status_of_enquiry == 'Registered' and self.student_registration_id==None:
            if self.office == 'Trivandrum':
                prefix = 'CBT'
                #self._meta.get_field('office').default='Trivandrum'
            elif self.office == 'kadavanthra':
                prefix = 'CB'
               # self._meta.get_field('office').default='kadavanthra'
            elif self.office == 'Calicut':
                prefix = 'CBC'
               # self._meta.get_field('office').default='Calicut'
            elif self.office == 'Bangalore':
                prefix = 'CBB'
               # self._meta.get_field('office').default='Bangalore'
            year = self.date_of_registration.year
            last_registered_student = Enquiry.objects.filter(status_of_enquiry='Registered', office=self.office).order_by('-student_registration_id').first()
            print(last_registered_student)
            if last_registered_student:
                last_registration_id = last_registered_student.student_registration_id
                last_registration_id_number = int(extract_numeric_part(last_registration_id))
                new_registration_id_number = last_registration_id_number + 1
            else:
                new_registration_id_number = 1
            new_registration_id = f"{prefix}{new_registration_id_number:04d}{year}"
            return new_registration_id
        return self.student_registration_id

    @registration_id.setter
    def registration_id(self, value):
        self.student_registration_id = value




# Signal to update the student_registration
@receiver(pre_save, sender=Enquiry)
def update_registration_id(sender, instance, **kwargs):
    instance.registration_id = instance.registration_id
def pre_save_outstanding_amount(sender, instance, **kwargs):
    instance.outstanding_amount = instance.total_amount - instance.total_amount_paid
    
    
class repeated_user(models.Model):
    name = models.CharField(max_length=40,blank=False)
    date_repeated =models.DateField(auto_now=True)
    last_enquiry_date = models.DateField(null=False)
    phone_number = models.CharField(max_length=15)
    
    
class Attendence(models.Model):
  #  id_of_attendence=models.AutoField(primary_key=True)
    #student_registration_id=models.ForeignKey(Student,on_delete=models.CASCADE,default=0)
    connection=models.ForeignKey(Enquiry, on_delete=models.CASCADE,null=True,blank=True)
    attendence_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=False)
    present=models.CharField(max_length=200,null=True)
    absent=models.CharField(max_length=50,null=True)
    objects=models.Manager()