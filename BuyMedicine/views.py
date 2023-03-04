from django.shortcuts import render,redirect
from .models import Medicine,orders
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def Medicine_Page(request):
    medicine=Medicine.objects.all()
    print(medicine)
    n=len(medicine)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides':nslides, 'range': range(1,nslides),'product': medicine}
    return render(request,'medicine.html',params)
    
@login_required
def checkout(request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            item_json=request.POST.get('item_json', '')
            state = request.POST.get('state', '')
            city = request.POST.get('city', '')
            zip = request.POST.get('zip', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address','')
            pay=request.POST.get('pay')
            ord = orders(item_json=item_json,name=name, phone=phone, email=email, state=state,city=city,zip=zip,address=address,)
            ord.save()
            thank=True
            id=ord.order_id
            return render(request,'payment_for_medicine.html',{'pay':pay})
        return render(request,'checkout.html')
