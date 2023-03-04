"""HospitalManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Doctor.views import doctor_details
from Dashbord.views import dashboard
from MainApp.views import MainApp
from Authenticating.views import Signin,Signup,signout
from Admin.views import Adminlogin
from adminpanel.views import adminpanel,AddDoctor
from Ward.views import addward
from Settings_.views import setting,delete,delete2
from Patient.views import patient_detail
from Payment.views import payment_detail,payment_for_consult,payment_for_medicine
from bookappointment.views import book_appointment
from Consult_Online.views import consult_online
from Ask.views import Ask_With_Us
from BuyMedicine.views import Medicine_Page,checkout
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor',doctor_details),
    path('dashboard',dashboard),
    path('',MainApp),
    path('signin',Signin),
    path('signup',Signup),
    path('loginasAdmin',Adminlogin),
    path('adminpanel',adminpanel),
    path('addDoctor',AddDoctor),
    path('addward',addward),
    path('setting',setting),
    path('delete/<int:id>/',delete,name="delete"),
    path('delete2/<int:id>/',delete2,name="delete2"),
    path('signout',signout),
    path('patient',patient_detail),
    path('payment',payment_detail),
    path('book_appointment',book_appointment),
    path('consult_online',consult_online),
    path('payment_for_consult',payment_for_consult),
    path('ask',Ask_With_Us),
    path('medicine',Medicine_Page),
    path('checkout',checkout),
    path('payment_for_medicine',payment_for_medicine)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
