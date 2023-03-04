from django.db import models

class Medicine(models.Model):
    product_id=models.AutoField
    category=models.CharField(max_length=50,default="")
    price = models.IntegerField( default="0")
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='images/',default="")

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000,default="")
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50,default="")
    address=models.CharField(max_length=500,default="")