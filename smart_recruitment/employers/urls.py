from django.urls import path
from . import views

urlpatterns=[
    
    path('', views.employers, name="employers")
    ]