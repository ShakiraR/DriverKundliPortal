from django.shortcuts import render
from driverkundliB2Bportal import views

# Create your views here.
def Home(request):
    return render(request,'driver_kundli_app/index.html')

def DriverList(request):
    return render(request,'driver_kundli_app/DriverList.html')

def AboutUs(request):
    return render(request,'driver_kundli_app/AboutUs.html')

def ContactUs(request):
    return render(request,'driver_kundli_app/ContactUs.html')

def JoinUs(request):
    return render(request,'driver_kundli_app/JoinUs.html')

def DriverDetails(request):
    return render(request,'driver_kundli_app/DriverDetails.html')

def Login(request):
    return render(request,'driver_kundli_app/Login.html')

def Signup(request):
    return render(request,'driver_kundli_app/Signup.html')

def Profile(request):
    return render(request,'driver_kundli_app/Profile.html')  

def SearchDrivers(request):
    return render(request,'driver_kundli_app/SearchDrivers.html')  

def Getdetails(request):
    return render(request,'driver_kundli_app/Getdetails.html')  

def MyDrivers(request):
    return render(request,'driver_kundli_app/MyDrivers.html')                        

