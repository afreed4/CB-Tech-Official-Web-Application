from django import forms
from django.forms import ModelForm

from . views import employi_db


class EmployeeForm(ModelForm):
    class Meta:
        model=employi_db
        fields=('emp_name','emp_email','emp_contact','emp_salary','emp_role')
        
        widgets={
        'emp_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
        'emp_email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        'emp_contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Number'}),
        'emp_salary':forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}),
        'emp_role':forms.TextInput(attrs={'class':'forms-control','placeholder':'Role'}),
        }