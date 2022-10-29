from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Applicant
from .forms import ApplicantForm

# applicantList = [

# {'id': '1', 'name': 'ikenna','jobtitle': 'devops engineer', 'description': 'Fully functional ecommerce website' },

# { 'id': '2', 'name': 'emeka','jobtitle': 'Web developer', 'description': 'A personal website to write articles and display work' },

# {'id': '3','name':'ebuka',  'jobtitle': 'Optician', 'description': 'An open source project built by the community' }

# ]


# Create your views here.
def loginUser(request):
    # if request.method == 'POST':
    #     username=requestself.POST['username']
    #     password=requestself.POST['password']
    # try:
        
        
    return render(request, 'applicants/login_register.html')

def applicants(request):
    applicants=Applicant.objects.all()
    context= {'applicants':applicants}
    return render(request, 'applicants/applicants.html',context)
    
def applicant(request, pk):
    
    applicantobj=Applicant.objects.get(id=pk)
    tags=applicantobj.tags.all()
    return render(request, 'applicants/single-applicant.html',{'applicant':applicantobj,'tags':tags})
    
def createApplicant(request):
    form= ApplicantForm()
    
    if request.method=="POST":
        form= ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applicants')
    context={'form' :form}
    return render(request, 'applicants/applicant_form.html', context)