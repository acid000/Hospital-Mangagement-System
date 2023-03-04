from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def doctor_details(request):
    return render(request,'doctor.html')
