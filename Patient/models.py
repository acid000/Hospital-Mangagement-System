from django.db import models

# Create your models here.
class PatientDetails(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    disease=models.CharField(max_length=1000)

