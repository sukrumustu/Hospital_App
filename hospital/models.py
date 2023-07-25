from django.db import models
from django.contrib.auth.models import User

class Professional_field(models.Model):
    name = models.CharField(max_length=50)
    
    
    
    
class Clinic(models.Model):
    name = models.CharField(max_length=50)
    
    
    
    

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_started = models.DateTimeField(auto_now_add=True)
    professional_field=models.ForeignKey(Professional_field, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)



    

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identity = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    
    
    
