from typing import Any
from django.db import models
import datetime
#from serializers import MessageConstantsSerializer

class Activity(models.Model):
    name=models.CharField(max_length=900,null=False,blank=False)
    discription=models.CharField(max_length=900,null=False,blank=False)
    slug=models.AutoField(primary_key=True)
    activity_type=(
        ('Event','Event'),
        ('Class','Class'),
        ('Venue','Venue'),
    )
    
    activity=models.CharField(max_length=500,null=False,blank=False,choices=activity_type)
    
    def __str__(self):
        return self.name,self.activity
    
   # class Meta:
     #   abstract=True

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    parent_tag_choice=(
        ('Social Events','Social Events'),
        ('Cultural Events','Cultural Events'),
        ('Educational Events','Educational Events'),
        ('Sporting Events','Sporting Events'),
        ('Political Events','Political Events'),
        ('Entertainment Events','Entertainment Events'),
        ('Fundraising Events','Fundraising Events')
    )
    parent_tag=models.CharField(max_length=600,null=False,blank=False,choices=parent_tag_choice)
    location=models.CharField(max_length=600,null=False,blank=False)
    gender_choice=(
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=60,choices=gender_choice)
    #-------------------------(contact)-----------------------------
    email=models.EmailField()
    mobile=models.CharField(max_length=20,null=False,blank=False)
    #-------------------------(end contact)-----------------------------
    priority_choice=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    priority=models.IntegerField(choices=priority_choice)
    booking_type=(
        ('Ticket','Ticket'),
        ('Slot','Slot'),
    )
    booking=models.CharField(max_length=90,choices=booking_type,null=False,blank=False)
    public_orgnaization_type=(
        ('National Geographic Society','National Geographic Society'),
        ('Red Cross/Red Crescent Societies','Red Cross/Red Crescent Societies'),
        ('Greenpeace','Greenpeace'),
        ('Amnesty International','Amnesty International'),
        ('Smithsonian Institution','Smithsonian Institution'),
        ('World Wildlife Fund (WWF)','World Wildlife Fund (WWF)'),
        ('European Space Agency (ESA)','European Space Agency (ESA):')
    )
    public_orgnaization=models.CharField(max_length=900,null=True,blank=True,choices=public_orgnaization_type)
    status_type=(
        ('Published','Published'),
        ('Not Published','Not Published')
    )
    status=models.CharField(max_length=100,null=False,blank=False,choices=status_type)
    capcity=models.IntegerField(default=1)
    landmark=models.CharField(max_length=900)
    
    def __init__(self):
       return self.status
   
    class Meta:
         abstract=True
       
   
class SportsAndArts(Event):
    #event_id=models.AutoField(primary_key=True)
    sports_type=(
        ("Basketball","Basketball"),
        ("Football","Football"),
        ("Swimming","Swimming"),
        ("Volley Ball","Volley Ball"),
        ('Music','Music')
    )
    select_sports=models.CharField(max_length=600,choices=sports_type,null=False,blank=False)
    stundent_leval_type=(
        ('Beginner','Beginner'),
        ('InterMediate','InterMediate'),
        ('Expert','Expert')
    )
    stundent_leval=models.CharField(max_length=500,null=False,blank=False,choices=stundent_leval_type)
    
    def __init__(self):
       return self.select_sports
   
   
class Venue(Event):
    pass


class ActivityDetails(models.Model):
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True,blank=True)
    event_img=models.ImageField(upload_to='event_pics')
   
    
    
    
        