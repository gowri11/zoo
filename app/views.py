from django.shortcuts import render,redirect

from .models import UserRegistration,AdminPersons1
from django.views.generic import ListView
from django.http import HttpResponse
#from django.core.mail import send_mail
from .forms import UserRegistrationform,loginform,AdminPersonsform,AdminLoginform


def hello(request):
    return render(request,'home.html')

def reg(request) :
    form = UserRegistrationform()
    if request.method=='POST' :
        form = UserRegistrationform(request.POST)
        if form.is_valid() :
            name = form.cleaned_data['name']
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            mobile_no = form.cleaned_data['mobile_no']
            country = form.cleaned_data['country']
            country_id = form.cleaned_data['country_id']
            ctnid_no = form.cleaned_data['ctnid_no']
            ud = UserRegistration(name=name,username=username,password=password,address=address,email=email,mobile_no=mobile_no,country=country,country_id=country_id,ctnid_no=ctnid_no)
            ud.save()
    return render(request,'register.html',{'form':form}) 


def login(request) :
    form=loginform()
    if request.method=='POST' :
        form = loginform(request.POST) 
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            dbuser=UserRegistration.objects.filter(username=username,password=password) 
            if not dbuser :
                return HttpResponse ("login failed") 
            else :
                return render(request,'success.html',{'form':form})
    return render(request,'login.html',{'form':form})




def adminPerson(request):
    form = AdminPersonsform()
    if request.method == 'POST':
        form = AdminPersonsform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            
            sur_name = form.cleaned_data['sur_name']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            mobile_no = form.cleaned_data['mobile_no']
            adhar_no = form.cleaned_data['adhar_no']
            ud1 = AdminPersons1(name=name,sur_name=sur_name,password=password,address=address,email=email,mobile_no=mobile_no,adhar_no=adhar_no)
            ud1.save()
    return render(request,'areg.html',{'form':form}) 


def alogin(request) :
    form=AdminLoginform()
    if request.method=='POST' :
        form = AdminLoginform(request.POST) 
        if form.is_valid() :
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            dbuser=AdminPersons1.objects.filter(name=name,password=password) 
            if not dbuser :
                return HttpResponse ("login failed") 
            else :
                return render(request,'booking.html',{'form':form})
    return render(request,'alog.html',{'form':form})
# Create your views here.
