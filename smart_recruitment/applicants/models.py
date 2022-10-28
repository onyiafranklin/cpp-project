from django.db import models
import uuid

class Applicant(models.Model):
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    email=models.EmailField(null=False, blank =False)
    address= models.TextField(null=False, blank =False, default="no address")
    profession_Title= models.CharField(max_length=200)
    gender= (
        ('male','male'),
        ('female','female'),
        ('choose no to say','choose not to say')
        )
    nationality= models.CharField(max_length=200,default="your country")
    skills=models.TextField(null=False, blank =False)
    gender= models.CharField(max_length=200,choices= gender, default="choose gender")
    source_link= models.CharField(max_length=200, null=True, blank= True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique= True, 
    primary_key= True, editable= False)
    
    def __str__(self):
        return self.firstname

# Create your models here.
