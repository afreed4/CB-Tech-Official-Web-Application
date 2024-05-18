from .models import CustomUser,Enquiry,Courses
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from django.core.validators import MaxLengthValidator
from datetime import datetime
from django.contrib.auth import get_user_model

def get_years_choices():
    current_year = datetime.now().year
    years_choices = [(str(year), str(year)) for year in range(2009, current_year + 1)]
    return years_choices

class PhoneNumberIntegerField(forms.IntegerField):
    def __init__(self, *args, **kwargs):
        # Add a MaxLengthValidator for 10 digits
        kwargs.setdefault('validators', []).append(MaxLengthValidator(limit_value=10))
        
        # Set the widget with desired attributes
        kwargs.setdefault('widget', forms.TextInput(attrs={
            'class': 'form-control class1',
            'placeholder': 'Phone Number',
            'maxlength': 10,  # Limit the input length to 10 characters
            'type': 'number', # Set input type to "number" to ensure numeric input
        }))
        
        super().__init__(*args, **kwargs)


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','gender','phone_number','alternate_phone_number','email_id','qualification','college','year_of_pass','technical_skills','lead_type','status_of_enquiry',
        'consultant_name','remarks','reference_name','reference_contact_number','office','mode_of_class','project_status','certificate','exam','course_type','course_completion','placement_session_attended']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Name'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Phone Number','id':'phone_number'}),
            'alternate_phone_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Alternate Contact Number','id':'phone_number1'}),
            'email_id':forms.EmailInput(attrs={'class': 'form-control class1', 'placeholder': 'Email Id'}),
            'qualification':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Qualification'}),
            'college':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'College Name'}),
            'technical_skills':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Technical Skills'}),
            'remarks':forms.Textarea(attrs={'class': 'form-control class1', 'placeholder':'Student Remark'}),
            'lead_type':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Lead Type'}),
            'reference_name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Reference Name'}),
            'reference_contact_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'reference contact number','id':'phone_number2'}),
           
            'mode_of_class':forms.Select(choices=[('Online','Online'),('Offline','Offline')],attrs={'class': 'form-control class1', 'placeholder':'Mode Of Class'}),
            'project_status':forms.Select(choices=[('Submitted','Submitted'),('Not Submitted','Not Submitted')],attrs={'class': 'form-control class1', 'placeholder':'Project Status'}),
            'certificate':forms.Select(choices=[('Received','Received'),('Not Received','Not Received')],attrs={'class': 'form-control class1', 'placeholder':'Certificate'}),
            'exam':forms.Select(choices=[('Finished','Finished'),('Not Finished','Not Finished')],attrs={'class': 'form-control class1', 'placeholder': 'Exam Status'}),
            'course_type':forms.Select(choices=[('Project','Project'),('Crash','Crash'),('Full Time','Full Time')],attrs={'class':'form-control class1','placeholder':'Course Type'}),
            'course_completion':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Course Completion'}),
            'placement_session_attended':forms.Select(choices=[('Yes','Yes'),('No','No')],attrs={'class':'form-control class1','placeholder':'Placement Session Attended'}),
            
        }
        user_choices = []
        year_of_pass = forms.ChoiceField(
            choices=get_years_choices(),
            widget=forms.Select(attrs={'class': 'form-control class1'}),
        )
        
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        self.user = user  # Store the user in the instance
        
        super(EnquiryForm, self).__init__(*args, **kwargs)
        
        self.status_choice = [('NotContacted','Not Contacted'),('Contacted','Contacted'),('Pending','Pending'),('NotInterested','Not Interested'),('Registered','Registered')]
        self.gender_choice = [('',''),('Male','Male'),('Female','Female'),('Others','Others')]
        custom_users = CustomUser.objects.filter(staff_type='counsellor')
        self.user_choices = [(user.first_name, user.first_name) for user in custom_users]
        self.office_choice= [('Kadavanthra','Kadavanthra'),('Trivandrum','Trivandrum'),('Calicut','Calicut'),('Bangalore','Bangalore')]


        self.fields['gender'] = forms.ChoiceField(
            choices=self.gender_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['consultant_name'] = forms.ChoiceField(
            choices=self.user_choices,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['status_of_enquiry'] = forms.ChoiceField(
            choices=self.status_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['year_of_pass'] = forms.ChoiceField(
            choices=get_years_choices(),
            widget=forms.Select(attrs={'class': 'form-control class1'}),
        )
        self.fields['office'] = forms.ChoiceField(
            choices=self.office_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        
    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.user:
            instance.updated_by = str(self.user)
        instance.updated_date = datetime.now()

        if commit:
            instance.save()

        return instance
    
class RegisteredForm(forms.ModelForm,forms.Form):
    class Meta:
        model = Enquiry
        fields = ['name','phone_number','email_id','gender','guardian_name','alternate_phone_number','address',
                'college','qualification','year_of_pass','technical_skills',
                'enquiry_id','lead_type','status_of_enquiry','remarks',
                'mode_of_class','profile_pic','date_of_registration',
                'course','course_type','course_status','total_amount','payment_status','number_of_installments','total_amount_paid',
                'next_due_date','payment_method','payment_History','declaration','declaration_type','consultant_name'
                ,'faculty_name','reference_name','reference_contact_number','marketing_manager','office']
        widgets = {
                'name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Name'}),
                'phone_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Contact Number','id':'phone_number'}),
                'email_id':forms.EmailInput(attrs={'class': 'form-control class1', 'placeholder': 'Email Id'}),
                'guardian_name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Guardian Name'}),
                'alternate_phone_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'alternative contact number','id':'phone_number'}),
                'address':forms.Textarea(attrs={'class': 'form-control class1', 'placeholder': 'Full Address'}),
                'college':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'College Name'}),
                'qualification':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Qualification'}),
                'technical_skills':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Technical Skills'}),
                'lead_type':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Lead Type'}),         
                'remarks':forms.Textarea(attrs={'class': 'form-control class1', 'placeholder': 'Student Remarks'}),
                'profile_pic':forms.ClearableFileInput(attrs={'class': 'form-control class1', 'placeholder': 'Image'}),
                'date_of_registration':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control class1'}),
                'total_amount':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Total amount'}),
                'number_of_installments':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Total amount'}),
                'next_due_date':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control class1'}),
                'payment_History':forms.Textarea(attrs={'class': 'form-control class1', 'placeholder': 'Payment Details'}),
                'amount_paid':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Total amount Paid'}),
                'amount':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Amount'}),
                'course_duration':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Course Duration'}),
                'marketing_manager':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Manager Name'}),
                'reference_name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Reference Name'}),
                'reference_contact_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Reference contact number'}),
                'course_type':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Course Duration'})
               
            }
    user_choices = []
    user_choices1 = []
    user_choices2 = []


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        self.user = user  # Store the user in the instance
        super(RegisteredForm, self).__init__(*args, **kwargs)

        custom_users = CustomUser.objects.filter(staff_type='counsellor')
        self.user_choices = [(user.first_name, user.first_name) for user in custom_users]
        faculty = CustomUser.objects.filter(staff_type='faculty')
        self.user_choices1 = [(user.first_name, user.first_name) for user in faculty]
        manager = CustomUser.objects.filter(staff_type='marketing manager')
        self.user_choices2 = [(user.first_name, user.first_name) for user in manager]
        self.status_choice = [('NotContacted','Not Contacted'),('Contacted','Contacted'),('Pending','Pending'),('NotInterested','Not Interested'),('Registered','Registered')]
        self.gender_choice = [('Male','Male'),('Female','Female')]
        self.mode_choice = [('Online','Online'),('Offline','Offline')]
        courses = Courses.objects.all()
        self.course_choice = [(course.course_name,course.course_name) for course in courses]
        self.course_type_choice = [('Full Time','Full Time'),('Crash','Crash'),('Project','Project')]
        self.course_status_choice = [('Joined','Joined'),('Persuing','Persuing'),('Completed','Completed'),('Dropped','Dropped')]
        self.payment_status_choice = [('Not Paid','Not Paid'),('Paid','Paid'),('EMI','EMI'),('Partially Paid','Partially Paid')]
        self.payment_method_choice = [('UPI','UPI'),('Internet_Banking','Internet Banking'),('Bank_Transfer','Bank Transfer'),('Cash','Cash')]
        self.declaration_choice = [('Yes','Yes'),('No','No')]
        self.declaration_type_choice = [('Manual','Manual'),('Digital','Digital')]
        self.office_choice= [('kadavanthra','kadavanthra'),('Trivandrum','Trivandrum'),('Calicut','Calicut'),('Bangalore','Bangalore')]

        self.fields['gender'] = forms.ChoiceField(
            choices=self.gender_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['year_of_pass'] = forms.ChoiceField(
            choices=get_years_choices(),
            widget=forms.Select(attrs={'class': 'form-control class1'}),
        )
        self.fields['status_of_enquiry'] = forms.ChoiceField(
            choices=self.status_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'}),
        )
        self.fields['mode_of_class'] = forms.ChoiceField(
            choices=self.mode_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'}),
        )
        self.fields['course'] = forms.ChoiceField(
            choices=self.course_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['course_type'] = forms.ChoiceField(
            choices=self.course_type_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['course_status'] = forms.ChoiceField(
            choices=self.course_status_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['payment_status'] = forms.ChoiceField(
            choices=self.payment_status_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['payment_method'] = forms.ChoiceField(
            choices=self.payment_method_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['consultant_name'] = forms.ChoiceField(
            choices=self.user_choices,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['faculty_name'] = forms.ChoiceField(
            choices=self.user_choices1,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['faculty_name'] = forms.ChoiceField(
            choices=self.user_choices1,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['marketing_manager'] = forms.ChoiceField(
            choices=self.user_choices2,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['declaration'] = forms.ChoiceField(
            choices=self.declaration_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['declaration_type'] = forms.ChoiceField(
            choices=self.declaration_type_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        self.fields['office'] = forms.ChoiceField(
            choices=self.office_choice,
            widget=forms.Select(attrs={'class': 'form-control class1'})
        )
    
      
    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.user:
            instance.updated_by = str(self.user)
        instance.updated_date = datetime.now()

        if commit:
            instance.save()

        return instance,super(RegisteredForm, self).save(commit=commit)


class Update_password_form(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'label': 'Current Password', 'placeholder': 'Current Password','name':'current_password','autocomplete':"off"}))
    new_password = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'label': 'New Password', 'placeholder': 'New Password','name':'new_password'}))
    repeat_new_password = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'label': 'Repeat Password', 'placeholder': 'Repeat New Password','name':'repeat_password'}))
    labels = {
        'current_password':'Current_password',
        'new_password':'New_password',
        'repeat_new_password':'repeat_new_password',
    }

class accountantform(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'name','phone_number','date_of_registration','number_of_installments','total_amount','total_amount_paid','outstanding_amount',
            'payment_date','amount','payment_receipt_number','next_due_date','payment_status','payment_History','payment_method','course','course_status','consultant_name','faculty_name',
            'payment_date','marketing_manager','office',
        ]
        widgets ={
            'name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Name'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Contact Number'}),
            'date_of_registration':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control class1'}),
            'total_amount':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Total amount',}),
            'total_amount_paid':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Total Amount Paid',}),
            'outstanding_amount':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'outstanding Amount','readonly':'true'}),
            'number_of_installments':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Number of Installments'}),
            'next_due_date':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control class1'}),
            'amount':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Amount'}),
            'payment_History':forms.Textarea(attrs={'class': 'form-control class1', 'placeholder': 'Payment History'}),
            'payment_receipt_number': forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Payment Reciept Number'}),
            'payment_date':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control class1'}),
            'course':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Course','readonly':'true'}),
        }
        user_choices = []
        user_choices1 = []
        
    def __init__(self, *args, **kwargs):
            super(accountantform, self).__init__(*args, **kwargs)
            custom_users = CustomUser.objects.filter(staff_type='counsellor')
            self.user_choices = [(user.first_name, user.first_name) for user in custom_users]
            print(custom_users,"custom users")
            faculty = CustomUser.objects.filter(staff_type='faculty')
            self.user_choices1 = [(user.first_name, user.first_name) for user in faculty]   
            manager = CustomUser.objects.filter(staff_type='marketing manager')
            self.user_choices2 = [(user.first_name, user.first_name) for user in manager]
            self.payment_method_choice = [('UPI','UPI'),('Internet_Banking','Internet Banking'),('Bank_Transfer','Bank Transfer'),('Cash','Cash')]
            self.payment_status_choice = [('Not Paid','Not Paid'),('Paid','Paid'),('EMI','EMI'),('Partially Paid','Partially Paid')]
            self.course_status_choice = [('Joined','Joined'),('Persuing','Persuing'),('Completed','Completed'),('Dropped','Dropped')]
            
            self.fields['consultant_name'] = forms.ChoiceField(
                choices=self.user_choices,
                widget=forms.Select(attrs={'class': 'form-control class1 '}),
                disabled=False,
            )
            self.fields['faculty_name'] = forms.ChoiceField(
                choices=self.user_choices1,
                widget=forms.Select(attrs={'class': 'form-control  class1 '}),
                disabled=False,
            )
            self.fields['office'].widget.attrs.update({
                'class': 'form-control class1',  # Add your desired CSS class name
                'placeholder': 'Offices',  # Add your placeholder text
                'Disabled':'False',
            })
            self.fields['course_status'] = forms.ChoiceField(
                choices=self.course_status_choice,
                widget=forms.Select(attrs={'class': 'form-control  class1 '}),
                disabled=False,
            )
            self.fields['payment_method'].widget.attrs.update({
                'class': 'form-control class1',  # Add your desired CSS class name
                'placeholder': 'Method Of Payment',  # Add your placeholder text
            })
            self.fields['payment_status'] = forms.ChoiceField(
                choices=self.payment_status_choice,
                widget=forms.Select(attrs={'class': 'form-control  class1 '}),
            )

            self.fields['marketing_manager'] = forms.ChoiceField(
                choices=self.user_choices2,
                widget=forms.Select(attrs={'class': 'form-control class1'}),
                disabled=False,
            )
            self.fields['payment_method'] = forms.ChoiceField(
                choices=self.payment_method_choice,
                widget=forms.Select(attrs={'class': 'form-control class1'})
            )
           

         