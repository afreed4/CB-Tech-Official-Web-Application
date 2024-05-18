from .models import CustomUser,Courses,RepeatedUser,Enquery
from django import forms
from django.core.validators import MaxLengthValidator
from datetime import datetime

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
        
        
class CostumUserForm(forms.ModelForm):
    class Meta:
      model=CustomUser
      fields=['staff_type','contact_number']
    
      widgets={
        'staff_type':forms.Select(attrs={'class':'custom-select'}),
        'contact_number':forms.NumberInput(attrs={'class':'form-control'})
      }
        
class CourseForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields=['course_type','course_duration','updated_at','course_name']
        
        widgets={
            
            'course_type':forms.Select(attrs={'class':'custom-select'}),
            'course_duration':forms.NumberInput(attrs={'class':'form-control'}),
            'updated_at':forms.DateInput(attrs={'class':'form-control', 'placeholder':'YY-MM-DD'})
        }

class RepeatedUserForm(forms.ModelForm):
    class Meta:
        model=RepeatedUser
        fields=['name','last_enquiry_date','phone_number']
        
        widgets={
            'name':forms.TextInput(),
            'last_enquiry_date':forms.DateInput(attrs={'placeholder':'YY-MM-DD'}),
            'phone_number':forms.TextInput()
        }
        
class RegisteredForm(forms.ModelForm,forms.Form):
    class Meta:
        model = Enquery
        fields = ['name','phone_number','email_id','gender','guardian_name','alternate_phone_number','address',
                'college','qualification','year_of_pass','technical_skills','profile_pic','status_of_enquiry','mode_of_class','date_of_registration','course','course_type','consultant_name','reference_name','reference_contact_number','office']
        
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
                'profile_pic':forms.ClearableFileInput(attrs={'class': 'form-control class1', 'placeholder': 'Image'}),
               
                'date_of_registration':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control class1'}),
                'joined_date':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control class1'}),
                'reference_name':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Reference Name'}),
                'reference_contact_number':forms.TextInput(attrs={'class': 'form-control class1', 'placeholder': 'Reference contact number'}),
            }
    user_choices = []
    user_choices1 = []
    user_choices2 = []
    
    year_of_pass = forms.ChoiceField(
      choices=get_years_choices(),
      widget=forms.Select(attrs={'class': 'form-control class1'}),
    )
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        self.user = user  # Store the user in the instance
        super(RegisteredForm, self).__init__(*args, **kwargs)
        
        custom_users = CustomUser.objects.filter(staff_type='counsellor')
        self.user_choices = [(user.first_name, user.first_name) for user in custom_users]
        
        self.fields['consultant_name'] = forms.ChoiceField(
          choices=self.user_choices,
          widget=forms.Select(attrs={'class': 'form-control class1'})
        )
        
        self.fields['consultant_name'] = forms.ChoiceField(
          choices=self.user_choices,
          widget=forms.Select(attrs={'class': 'form-control class1'})
        )