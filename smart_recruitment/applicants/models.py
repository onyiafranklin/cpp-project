from django.db import models
import uuid
from django.contrib.auth.models import User

class Applicant(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    profile_picture= models.ImageField(null=False, blank =False,default= "default-pp.JPG")
    email=models.EmailField(null=False, blank =False)
    address= models.TextField(null=False, blank =False, default="no address")
    profession_Title= models.CharField(max_length=200)
    about=models.TextField(null=False, blank =False, default= "short note about self")
    gender= (
        ('male','male'),
        ('female','female'),
        ('choose no to say','choose not to say')
        )
    nationality= models.CharField(max_length=200,default="your country")
    skills=models.TextField(null=False, blank =False)
    gender= models.CharField(max_length=200,choices= gender, default="choose gender")
    source_link= models.CharField(max_length=200, null=True, blank= True)
    tags=models.ManyToManyField('Tag', blank=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique= True, 
    primary_key= True, editable= False)
    
    def __str__(self):
        return self.firstname
        
        
class Tag(models.Model):
    name= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique= True, 
    primary_key= True, editable= False)
    
    def __str__(self):
        return self.name

# Create your models here.
