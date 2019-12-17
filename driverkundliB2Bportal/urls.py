from django.contrib import admin
from django.urls import path
from driverkundliB2Bportal import views

urlpatterns = [
    path("Home", views.Home, name="Home"),

    path("DriverList", views.DriverList, name="DriverList"),

    path("AboutUs", views.AboutUs, name="AboutUs"),

    path("ContactUs", views.ContactUs, name="ContactUs"),

    path("JoinUs", views.JoinUs, name="JoinUs"),

    path("DriverDetails", views.DriverDetails, name="DriverDetails"),

    path("Login", views.Login, name="Login"),

    path("Signup", views.Signup, name="Signup"),

    path("Profile", views.Profile, name="Profile"),

    path("SearchDrivers", views.SearchDrivers, name="SearchDrivers"),

    path("Getdetails", views.Getdetails, name="Getdetails"),

    path("MyDrivers", views.MyDrivers, name="MyDrivers"),

    
]
