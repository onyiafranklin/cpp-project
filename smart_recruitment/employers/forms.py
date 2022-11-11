from django.forms import ModelForm
from .models import Employer
from django import forms

class ApplicantForm(ModelForm):
    class Meta:
        model= Applicant
        fields= ['firstname','lastname', 'email','address','profession_Title','about','gender','nationality','skills','source_link','tags','profile_picture']
    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args,**kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})