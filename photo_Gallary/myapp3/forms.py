from .models import Albums,AlbumDetailView
from django import forms

class PhotoForm(forms.ModelForm):
     class Meta:
         model=Albums
         exclude=[]
         
     zip=forms.FileField(required=False)