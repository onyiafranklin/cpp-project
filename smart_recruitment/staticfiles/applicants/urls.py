from django.urls import path,include
from . import views

urlpatterns=[
    #path('login', views.loginUser, name= "login" ),
    path('',views.applicants, name ='applicants'),
    path('applicants/<str:pk>',views.applicant, name= 'applicant'),
    path('create-applicant/',views.createApplicant, name= 'create-applicant'),
    path('update-applicant/<str:pk>/',views.updateApplicant, name= 'update-applicant'),
    path('delete-applicant/<str:pk>/',views.deleteApplicant, name= 'delete-applicant'),
    ]