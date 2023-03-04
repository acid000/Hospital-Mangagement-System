from django.shortcuts import render
from .models import WardDetail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addward(request):
    if request.method=='POST':
        total_size=request.POST.get('totalsize')
        available_size=request.POST.get('available')
        new_ward=WardDetail(total_size=total_size,available_size=available_size)
        new_ward.save()
    return render(request,'add_ward.html')
