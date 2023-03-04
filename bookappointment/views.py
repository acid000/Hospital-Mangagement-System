from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
# Create your views here.
dict={}
@login_required
def book_appointment(request):
    
    uid=random.randint(1,9)
    while uid in dict:
        uid=random.randint(1,9)
    dict[uid]=True
    context={'token':uid}    
    return render(request,'book_appointment.html',context)
