from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=['name','phone_num','patient_relative_name','patient_relative_contact','address','symptoms','prior_ailments','bed_num','dob','doctor','doctors_notes','doctors_visiting_time','status']

admin.site.register(Patient,PatientAdmin)

class BedAdmin(admin.ModelAdmin):
    list_display=['bed_number','occupied'] 

admin.site.register(Bed,BedAdmin)   
admin.site.register(Doctor) 

class BillAdmin(admin.ModelAdmin): 
    list_display=['name','email','addr','city','state','zip']

admin.site.register(Bill,BillAdmin)     

class PaymentAdmin(admin.ModelAdmin): 
    list_display=['amount','payment_mode'] 

admin.site.register(Payment,PaymentAdmin)     