from django.db import models

class Admin(models.Model):
    username=models.CharField(max_length=12)
    name=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=16,default="raju@0")
    

