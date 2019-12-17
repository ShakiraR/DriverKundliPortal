from django.contrib import admin
from driverkundliB2Bportal.models import Vendor,Review,Driver

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("Vendor_Name","Vendor_Organisation", "Vendor_Address","Vendor_PhoneNo", "Vendor_Email","Vendor_profile_image")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("Review_by","Review_To", "Review_Message","Review_Date")

class DriverAdmin(admin.ModelAdmin):
    list_display = ("driver_reference_no",
                    "driver_driver_name",
                    "driver_vehicle_type",
                    "vehicle_type_of_module",
                    "driver_joining_date",
                    "driver_license_number",
                    "driver_aadhar_number",
                    "driver_contact_number",
                    "driver_pan_number",
                    "driver_address_proof",
                    "driver_photoid_proof",
                    "driver_driver_bank_name",
                    "driver_bank_name",
                    "driver_bank_account_number",
                    "driver_ban_ifsc_code",
                    "driver_bank_branch",
                    "driver_alternate_contact_number",
                    "driver_license_residence_address",
                    "driver_aadhar_card_residence_address",
                    "driver_years_of_experience",
                    "driver_last_employer_name",
                    "driver_profile_image")    

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Driver)



