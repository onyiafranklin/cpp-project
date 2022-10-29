from django.forms import ModelForm
from .models import Applicant

class ApplicantForm(ModelForm):
    class Meta:
        model= Applicant
        fields= ['firstname','lastname', 'email','address','profession_Title','gender','nationality','skills','source_link','tags']
        