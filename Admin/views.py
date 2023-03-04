from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import Admin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@csrf_protect


def Adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        try:
            adminuser=Admin.objects.get(username=username)
        except:
            return redirect('/')
        if  adminuser.password==pass1 :
            user = authenticate(username=username, password=pass1)
            login(request, user)
            return redirect('/adminpanel')
        else:
            return redirect('/')
    
    return render(request, "adminlogin.html")

