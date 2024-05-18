from django import forms
from . models import Activity,Event,SportsAndArts,Venue,ActivityDetails
from time import timezone

class ActivityForm(forms.Form):
    class Meta:
        model=Activity
        fields=['name','discription','activity','slug']
        
        widgets={
            'name':forms.CharField(max_length=200,label='Name'),
            'discription':forms.CharField(label='discription'),
            'activity':forms.Select(choices=[('Event','Event'),('Class','Class'),('Venue','Venue')],attrs={'class': 'form-control class1', 'placeholder': 'activity_type'}),
            'slug':forms.Textarea()
            
            }
            
            
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['parent_tag','location','gender','email','mobile','priority','booking','public_orgnaization','status','capcity','landmark']
        
        widgets={
            'parent_tag':forms.Select(choices=[('Social Events','Social Events'),('Cultural Events','Cultural Events'),('Educational Events','Educational Events'),('Sporting Events','Sporting Events'),('Political Events','Political Events'),('Entertainment Events','Entertainment Events'),('Fundraising Events','Fundraising Events')],attrs={'class': 'form-control class1', 'placeholder': 'activity_type'}),
           
            'location':forms.Textarea(attrs={'placeholder':'Location'}),
            'gender':forms.Select(choices=[('Male','Male'),('Female','Female'),('Others','Others')]),
            'email':forms.Textarea(attrs={'placeholder':'Email'}),
            'mobile':forms.NumberInput(attrs={'placeholder':'Mobile'}),
            'priority':forms.Select(choices=[('1','1'),('2',2),('3',3),('4','4')]),
            'booking':forms.Select(choices=[('Ticket','Ticket'),('Slot','Slot')]),
            'public_orgnaization':forms.Select(choices=[('National Geographic Society','National Geographic Society'), ('Red Cross/Red Crescent Societies','Red Cross/Red Crescent Societies'),('Greenpeace','Greenpeace'),('Amnesty International','Amnesty International'),('Smithsonian Institution','Smithsonian Institution'),('World Wildlife Fund (WWF)','World Wildlife Fund (WWF)'),('European Space Agency (ESA)','European Space Agency (ESA)')]),
            'status_type':forms.Select(choices=(('Published','Published'),('Not Published','Not Published'))),
            'capcity':forms.NumberInput(attrs={'placeholder':'Capacity'},),
            'landmark':forms.Textarea(attrs={'placeholder':'LandMark'})
        }
        
        
class SportAndArtsForm(forms.ModelForm):
    class Meta:
        model=SportsAndArts
        fields='__all__'
        
        widgets={
            'select_sports':forms.Select(choices=[("Basketball","Basketball"),("Football","Football"),("Swimming","Swimming"),("Volley Ball","Volley Ball"),('Music','Music')]),
           
            'location':forms.Textarea(attrs={'placeholder':'Location'}),
            'gender':forms.Select(choices=[('Male','Male'),('Female','Female'),('Others','Others')]),
            'email':forms.Textarea(attrs={'placeholder':'Email'}),
            'mobile':forms.NumberInput(attrs={'placeholder':'Mobile'}),
            'priority':forms.Select(choices=[('1','1'),('2',2),('3',3),('4','4')]),
            'booking':forms.Select(choices=[('Ticket','Ticket'),('Slot','Slot')]),
            'public_orgnaization':forms.Select(choices=[('National Geographic Society','National Geographic Society'), ('Red Cross/Red Crescent Societies','Red Cross/Red Crescent Societies'),('Greenpeace','Greenpeace'),('Amnesty International','Amnesty International'),('Smithsonian Institution','Smithsonian Institution'),('World Wildlife Fund (WWF)','World Wildlife Fund (WWF)'),('European Space Agency (ESA)','European Space Agency (ESA)')]),
            'status_type':forms.Select(choices=(('Published','Published'),('Not Published','Not Published'))),
            'capcity':forms.NumberInput(attrs={'placeholder':'Capacity'}),
            'landmark':forms.Textarea(attrs={'placeholder':'LandMark'})
        }
        
class VenuForm(forms.ModelForm):
    class Meta:
        model=Venue
        fields='__all__'
        
        
        widgets={
            'parent_tag':forms.Select(choices=[('Social Events','Social Events'),('Cultural Events','Cultural Events'),('Educational Events','Educational Events'),('Sporting Events','Sporting Events'),('Political Events','Political Events'),('Entertainment Events','Entertainment Events'),('Fundraising Events','Fundraising Events')],attrs={'class': 'form-control class1', 'placeholder': 'activity_type'}),

            'location':forms.Textarea(attrs={'placeholder':'Location'}),
            'gender':forms.Select(choices=[('Male','Male'),('Female','Female'),('Others','Others')]),
            'email':forms.Textarea(attrs={'placeholder':'Email'}),
            'mobile':forms.NumberInput(attrs={'placeholder':'Mobile'}),
            'priority':forms.Select(choices=[('1','1'),('2',2),('3',3),('4','4')]),
            'booking':forms.Select(choices=[('Ticket','Ticket'),('Slot','Slot')]),
            'public_orgnaization':forms.Select(choices=[('National Geographic Society','National Geographic Society'), ('Red Cross/Red Crescent Societies','Red Cross/Red Crescent Societies'),('Greenpeace','Greenpeace'),('Amnesty International','Amnesty International'),('Smithsonian Institution','Smithsonian Institution'),('World Wildlife Fund (WWF)','World Wildlife Fund (WWF)'),('European Space Agency (ESA)','European Space Agency (ESA)')]),
            'status_type':forms.Select(choices=(('Published','Published'),('Not Published','Not Published'))),
            'capcity':forms.NumberInput(attrs={'placeholder':'Capacity'}),
            'landmark':forms.Textarea(attrs={'placeholder':'LandMark'})
        }
        
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model=ActivityDetails
        fields='__all__'
        
        widgets={
            'start_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'class': 'datepicker'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='start_date'),
            'end_date':forms.DateField( help_text='Enter a date in the format YYYY-MM-DD',
                                                                     required=True,
                                                                     disabled=False,
                                                                     widget=forms.DateInput(attrs={'class': 'datepicker'}),
                                                                     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
                                                                     validators=[],label='end_date'),
            'start_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='start_time'),
            'end_time':forms.TimeField( input_formats=['%H:%M:%S', '%H:%M', '%I:%M %p'],label='end_time'),
            'event_img':forms.ImageField(label='Image'),
        }