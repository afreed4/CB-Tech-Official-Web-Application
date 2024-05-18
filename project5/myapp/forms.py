from django import forms
from . models import *

class Profile(forms.ModelForm):
    class Meta:
        model=Profile_DB
        fields=('profile_img','bio','phone','instagram','linkdin','facebook')
        
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blogpost_DB
        fields=('title','blog_img','slug','content','blog_img')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog'}),
            'slug':forms.TextInput(attrs={'class':'form-control','placehlder':'Copy the title with no space and a hyphen in between'}),
            'content':forms.TextInput(attrs={'class':'form-control','placeholder':'Content of the Blog'})
        }
