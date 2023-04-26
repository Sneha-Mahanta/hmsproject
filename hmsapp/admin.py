from django.contrib import admin 
from hmsapp.models import * 
# Register your models here. 
class IpdRegisterAdmin(admin.ModelAdmin): 
    
    list_display=[
    'ipd_no',
    'patient_name', 
    'blood_group',
    'department',
    'doctor',
    'bed_group',
    'bed_no', 
    'symptoms',   
    ]        
admin.site.register(IpdRegister,IpdRegisterAdmin)  
 
class OpdRegisterAdmin(admin.ModelAdmin):
    list_display=['patient_name','blood_group','sex','department','asigned_doctor']

admin.site.register(OpdRegister,OpdRegisterAdmin)

class MedicineRegisterAdmin(admin.ModelAdmin):
    list_display=['medicine_name','comapny_name','medicine_category','medicine_group','pack','unit_pack']
admin.site.register(Medicine_register,MedicineRegisterAdmin)

class TestRegisterAdmin(admin.ModelAdmin):
    list_display=['patient_name','blood_group','department','doctor','testcase']
admin.site.register(TestRegister,TestRegisterAdmin)    