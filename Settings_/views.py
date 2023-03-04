from django.shortcuts import render,redirect
from Doctor.models import Doctor_Details
from Ward.models import WardDetail
from Patient.models import PatientDetails
from django.contrib.auth.decorators import login_required

@login_required
def setting(request):
    doctor_list=Doctor_Details.objects.all()
    ward_list=WardDetail.objects.all()
    patient_list=PatientDetails.objects.all()
    dict={'doctor_list':doctor_list,'ward_list':ward_list,'patient_list':patient_list}
    return render(request,'setting.html',dict)

@login_required
def delete(request,id):
    print(str(id))
    try:
        item=Doctor_Details.objects.get(id=id)
        
        item.delete()
    
    except:
        print(str(id))
        print("not found")
    return redirect('/setting')

@login_required
def delete2(request,id):
    print(str(id))
    try:
        
        item=PatientDetails.objects.get(id=id)

        item.delete()
    
    except:
        print(str(id))
        print("not found")
    return redirect('/setting')    
    