from django.contrib import admin

# Register your models here.
from .models import Medicine,orders
admin.site.register(Medicine)
admin.site.register(orders)