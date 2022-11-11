from django.db import models
from django.contrib.auth.models import User
import uuid

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    employer_firstname= models.CharField(max_length=200)
    employer_lastname= models.CharField(max_length=200)
    organization_name= models.CharField(max_length=200)
    employer_email=models.EmailField(null=False, blank =False)
    employer_profile_picture = models.ImageField(
        null=True, blank=True, upload_to='employer_pic/', default="employer_pic/default-pp.JPG")
    organization_address= models.TextField(null=False, blank =False, default="no address")
    about=models.TextField(null=False, blank =False, default= "short note about self")
    source_link= models.CharField(max_length=200, null=True, blank= True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default= uuid.uuid4, unique= True, 
    primary_key= True, editable= False)
    
    def __str__(self):
        return self.organization_name
        