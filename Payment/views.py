from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def payment_detail(request):
    money_to_be_pay=500
    dict={'pay':money_to_be_pay}
    return render(request,'payment.html',dict)

@login_required
def payment_for_consult(request):
    money_to_be_pay=500
    dict={'pay':money_to_be_pay}
    return render(request,'payment_for_consult.html',dict)

@login_required
def payment_for_medicine(request):
    money_to_be_pay=500
    dict={'pay':money_to_be_pay}
    return render(request,'payment_for_medicine.html',dict)