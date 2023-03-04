from django.shortcuts import render,redirect
from .models import PatientDetails
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def patient_detail(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        disease=request.POST.get('disease')
        new_patient=PatientDetails(name=name,age=age,disease=disease)
        new_patient.save()
        return redirect('/payment')
    return render(request,'patient.html')