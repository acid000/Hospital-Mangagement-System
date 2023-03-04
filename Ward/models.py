from django.db import models

# Create your models here.
class WardDetail(models.Model):
    ward_id=models.AutoField(primary_key=True)
    total_size=models.IntegerField()
    available_size=models.IntegerField()
