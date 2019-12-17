from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Vendor(models.Model):
    Vendor_Name = models.CharField(max_length=264,blank=False)
    Vendor_Organisation = models.CharField(max_length=264,blank=False)
    Vendor_Address = models.CharField(max_length=264,blank=True)
    Vendor_PhoneNo = models.CharField(max_length=264,blank=False)
    Vendor_Email = models.EmailField(max_length=500,blank=False)
    Vendor_profile_image = models.ImageField(null=True, blank=True, upload_to="Image/")

class Review(models.Model):
    Review_by = models.CharField(max_length=264,blank=False)
    Review_To = models.CharField(max_length=264,blank=False)
    Review_Message = models.CharField(max_length=500,blank=False)
    Review_Date = models.DateTimeField(default=timezone.now)

class Driver(models.Model):
    driver_reference_no = models.IntegerField()
    driver_driver_name = models.CharField(max_length=264,default="")
    driver_vehicle_type = models.CharField(max_length=264,blank=True)
    vehicle_type_of_module = models.CharField(max_length=264,blank=True)
    driver_joining_date = models.DateTimeField(default=timezone.now)
    driver_license_number = models.CharField(max_length=264,blank=True)
    driver_aadhar_number = models.CharField(max_length=264,blank=True,default="")
    driver_contact_number = models.CharField(max_length=264,blank=True,default="")
    driver_pan_number = models.CharField(max_length=264,blank=True,default="")
    driver_address_proof = models.CharField(max_length=264,blank=True,default="")
    driver_photoid_proof = models.CharField(max_length=264,blank=True,default="")
    driver_driver_bank_name = models.CharField(max_length=264,default="")
    driver_bank_name = models.CharField(max_length=264,blank=True,default="")
    driver_bank_account_number = models.CharField(max_length=264,blank=True)
    driver_ban_ifsc_code = models.CharField(max_length=264,blank=True,default="")
    driver_bank_branch = models.CharField(max_length=264,blank=True,default="")
    driver_alternate_contact_number=models.CharField(max_length=264,blank=True,default="")
    driver_license_residence_address=models.CharField(max_length=264,blank=True,default="")
    driver_aadhar_card_residence_address=models.CharField(max_length=264,blank=True,default="")
    driver_years_of_experience = models.CharField(max_length=264,blank=True,default="")
    driver_last_employer_name = models.CharField(max_length=264,blank=True,default="")
    driver_profile_image = models.ImageField(null=True, blank=True, upload_to="driver_image/")

    def __str__(self):
                return str(self.driver_reference_no) 

# class CustomUser(AbstractUser):
#     SUPER_ADMIN = 1
#     ADMIN = 2
#     ROLE_CHOICES = (
#       (ADMIN,'admin'),
#       (SUPER_ADMIN,'super_admin')
#     )
#     user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)
#     Name = models.CharField(max_length=264, blank='True')
#     Organisation_Name = models.ForeignKey(Vendor,on_delete=models.CASCADE)
#     Email = models.EmailField(max_length=264)
#     Date_Of_Joining = models.DateTimeField(default=timezone.now)                   

