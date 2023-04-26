from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
                          
class OpdRegister(models.Model):
    patient_name= models.CharField(max_length=30)
    blood_group=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    department=models.CharField(max_length=30) 
    asigned_doctor=models.CharField(max_length=45) 
    fees=models.CharField(max_length=32)                     

class IpdRegister(models.Model):                           
    ipd_no=models.CharField(max_length=20)                 
    patient_name=models.CharField(max_length=20)                  
    blood_group=models.CharField(max_length=20)                     
    department=models.CharField(max_length=20)              
    doctor=models.CharField(max_length=20)                 
    bed_group=models.CharField(max_length=30)              
    bed_no=models.CharField(max_length=20)                 
    symptoms=models.CharField(max_length=20)               
    fees=models.FloatField()                               

class Medicine_register(models.Model): 
    medicine_name=models.CharField(max_length=20) 
    comapny_name=models.CharField(max_length=20) 
    medicine_category=models.CharField(max_length=20) 
    medicine_group=models.CharField(max_length=20)  
    pack=models.IntegerField() 
    unit_pack=models.IntegerField() 
    rupees=models.FloatField() 

class TestRegister(models.Model): 
    patient_name=models.CharField(max_length=20) 
    blood_group=models.CharField(max_length=20)  
    department=models.CharField(max_length=20)   
    doctor=models.CharField(max_length=20)        
    TESTCASE=(  
        ('fever','fever'), 
        ('cough','cough'), 
        ('diabetes','diabetes'), 
        ('hemoglobin','hemoglobin'), 
        ('vitamin','vitamin'),  
        ('urin','urin'),   
        ('Radiology X-ray','Radiology X-ray'), 
        ('MRI','MRI'), 
        ('thyroid','thyroid')  
    )                          
    testcase=MultiSelectField(choices=TESTCASE, null=True)  
    fees=models.FloatField() 