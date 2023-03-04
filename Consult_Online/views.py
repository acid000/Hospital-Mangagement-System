from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def consult_online(request):
    return render(request,'consult_online.html')
