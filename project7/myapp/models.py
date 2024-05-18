from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from django.utils import timezone
import random
from calendar import monthrange
import time
import re
# Create your models here.

curent_year=timezone.now().year

def extract_numeric_part(input_str):
    if input_str is None:
        return 0
    match = re.search(r'(\d{4})',input_str)
    if match:
        return match.group(1)
    else:
        return 0

class CustomUser(models.Model):
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
    
    def __str__(self):
	    return self.course_name
 
class RepeatedUser(models.Model):
    name = models.CharField(max_length=40,blank=False)
    date_repeated =models.DateField(auto_now=True)
    last_enquiry_date = models.DateField(null=False)
    phone_number = models.CharField(max_length=15)
    
class Enquery(models.Model):
    date_of_registration=models.DateField(blank=False,null=True,default=timezone.now)
    student_registration_id = models.CharField(max_length=40,blank=True,null=True,default=None)
    status_of_enquiry = models.CharField(max_length=15,default='Not Contacted',blank=True,null=True)
    name=models.CharField(max_length=180)
    address=models.CharField(max_length=800)
    email_id=models.CharField(max_length=300)
    gender = models.CharField(max_length=8,blank=True,null=True)
    guardian_name=models.CharField(max_length=40, blank=True,null=True)
    alternate_phone_number=models.CharField(blank=True,null=True,max_length=15)
    phone_number=models.CharField(blank=True,null=True,max_length=15)
    college=models.CharField(max_length=30,blank=True,null=True)
    qualification = models.CharField(max_length=30,blank=False,null=True)
    year_of_pass =models.IntegerField(null=False,blank=False,default=curent_year)
    technical_skills=models.CharField(max_length=60,blank=True,null=True)
    mode_of_class = models.CharField(max_length=10,blank=True,null=True)
    consultant_name = models.CharField(max_length=10,blank=False,null=False,default='')
    reference_name = models.CharField(max_length=40,blank=True,null=True)
    reference_contact_number = models.CharField(blank=True,null=True,default='',max_length=15)
    course = models.CharField(max_length=20,blank=True,null=True)
    course_type = models.CharField(max_length=10,null=True,blank=False)
    profile_pic=models.ImageField(upload_to = 'photos/', blank=True,null=True)
    OFFICE_TYPE=(
        ('Kadavanthra','Kadavanthra'),
        ('Trivandrum','Trivandrum'),
        ('Calicut','Calicut'),
        ('Bangalore','Bangalore')
    )
    office = models.CharField(max_length=13,blank=True,null=True,default='Kadavanthra',choices=OFFICE_TYPE)
    
    @property
    def registration_id(self):
        if self.status_of_enquiry == 'Registered' and self.student_registration_id==None:
            if self.office == 'Trivandrum':
                prefix = 'CBT'
            elif self.office == 'kadavanthra':
                prefix = 'CB'
            year = self.date_of_registration.year
            last_registered_student = Enquery.objects.filter(status_of_enquiry='Registered', office=self.office).order_by('-student_registration_id').first()
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
@receiver(pre_save, sender=Enquery)
def update_registration_id(sender, instance, **kwargs):
    instance.registration_id = instance.registration_id
def pre_save_outstanding_amount(sender, instance, **kwargs):
    instance.outstanding_amount = instance.total_amount - instance.total_amount_paid



