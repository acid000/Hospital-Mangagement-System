from django.db import models

class Doctor_Details(models.Model):
    name=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    experience=models.IntegerField()
    specialization=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)