from django.shortcuts import render
from Doctor.models import Doctor_Details
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required(login_url='/')
def adminpanel(request):

    return render(request,'adminpanel.html')

@staff_member_required(login_url='/')
def AddDoctor(request):
    if request.method=='POST':
        name=request.POST.get('name')
        degree=request.POST.get('degree')
        experience=request.POST.get('experience')
        specialization=request.POST.get('specialization')
        isavailable=request.POST.get('isavailable')
        print(specialization)
        if isavailable=='on':
            isavailable=True
        else:
            isavailable=False    
        
        newdoctor=Doctor_Details(name=name,degree=degree,experience=experience,specialization=specialization,is_available=isavailable)
        newdoctor.save()
        return redirect('/adminpanel')
    return render(request,'addDoctor.html')