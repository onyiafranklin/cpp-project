from django.urls import path,include
from . import views

urlpatterns=[
    #path('login', views.loginUser, name= "login" ),
    path('',views.applicants, name ='applicants'),
    path('applicants/<str:pk>',views.applicant, name= 'applicant'),
    path('createApplicant/',views.createApplicant, name= 'create-applicant'),
    
    
    ]