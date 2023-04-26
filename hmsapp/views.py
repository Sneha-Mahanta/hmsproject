from django.shortcuts import render,redirect
from hmsapp.models import *
from main.models import *
# Create your views here.

def ipdRegistrationView(request):
    patients =  Patient.objects.all()  
    doctor = Doctor.objects.all() 
    beds = Bed.objects.all() 
    context= {'patients':patients,'doctor':doctor,'beds':beds } 
    if request.method=='POST':  
        ipdno=request.POST.get('ipd_no')                          
        patient_name=request.POST.get('patient_name')               
        blood_group=request.POST.get('blood_group')                       
        department=request.POST.get('department')                    
        doctor=request.POST.get('doctor')                         
        bed_group=request.POST.get('bed_group')                      
        bed_no=request.POST.get('bed_no') 
        symptoms=request.POST.get('symptoms')                        
        fees=request.POST.get('fees')                                  
        ipd=IpdRegister(ipd_no=ipdno,patient_name=patient_name,blood_group=blood_group,department=department,doctor=doctor,bed_group=bed_group,bed_no=bed_no,symptoms=symptoms,fees=fees)  
        ipd.save()  
        print(ipd)
        return redirect('/ipd')        
    else:
        print("invalid choice")          
    return render(request,'hmsapp/ipd_register.html',context) 

def opd_RegisterView(request):
    patients= Patient.objects.all() 
    doctor= Doctor.objects.all() 
    context={'patients':patients,'doctor':doctor } 
    if request.method=='POST': 
        patientname =request.POST.get('patientname','') 
        bloodgroup =request.POST.get('blood_group','') 
        sex =request.POST.get('sex','') 
        department =request.POST.get('department','')  
        doctor =request.POST.get('doctor')  
        fees=request.POST.get('fees')   
        opdregister =OpdRegister(patient_name=patientname,blood_group=bloodgroup,sex=sex,department=department,asigned_doctor=doctor,fees=fees)
        opdregister.save()    
        return redirect('/opd') 
    else:  
        print('invalid choice')    
          
    return render(request,'hmsapp/opd_register.html',context) 

def medicineRegisterView(request):
    medicine=Medicine_register.objects.all()
    context={'medicine':medicine}   
    if request.method=='POST':
        medicine_name=request.POST.get('medicine_name') 
        comapny_name=request.POST.get('comapny_name') 
        medicine_category=request.POST.get('medicine_category')  
        medicine_group=request.POST.get('medicine_group') 
        pack=request.POST.get('pack') 
        unit_pack=request.POST.get('unit_pack') 
        rupees=request.POST.get('rupees')            
        medicine=Medicine_register(medicine_name=medicine_name,comapny_name=comapny_name,medicine_category=medicine_category,medicine_group=medicine_group,pack=int(pack),unit_pack=int(unit_pack),rupees=rupees)  
        medicine.save()  
        return redirect('/pharmacy')
    else: 
        print('invalid')                             
    return render(request,'hmsapp/medicine_register.html',context)  
                              
def ipd_details_id(request,id):                                            
    patient_ipd = IpdRegister.objects.get(id=id)
    return render(request,'hmsapp/ipd_details.html',{'patient_ipd':patient_ipd})

def opdUpdateView(request,id):
    patient= OpdRegister.objects.get(id=id)
    if request.method == "POST": 
        patient_name = request.POST['patient_name']
        blood_group = request.POST['blood_group']
        sex = request.POST['sex']
        department  = request.POST['department']
        asigned_doctor=request.POST['asigned_doctor']
        fees=request.POST['fees'] 
        patient.patient_name = patient_name 
        patient.blood_group = blood_group 
        patient.sex = sex 
        patient.department = department
        patient.asigned_doctor =asigned_doctor  
        patient.fees=fees      
        patient.save()
        return redirect('/opd') 
    else:  
        print('invalid')    
    context = {                             
        'patient': patient                   
    }                                                
    return render(request, 'hmsapp/opd_update.html', context)
                                                               
def ipdUpdateView(request,id): 
    patient_ipd = IpdRegister.objects.get(id=id)      
    if request.method == "POST": 
        ipd_no=request.POST['ipd_no']                    
        patient_name = request.POST['patient_name'] 
        blood_group = request.POST['blood_group']
        department  = request.POST['department']
        doctor=request.POST['doctor']                     
        bed_group=request.POST['bed_group']                
        bed_no=request.POST['bed_no']              
        symptoms=request.POST['symptoms']                 
        patient_ipd.ipd_no=ipd_no                                     
        patient_ipd.patient_name = patient_name            
        patient_ipd.blood_group = blood_group                     
        patient_ipd.department = department               
        patient_ipd.doctor = doctor                  
        patient_ipd.bed_group  = bed_group           
        patient_ipd.bed_no = bed_no              
        patient_ipd.symptoms = symptoms          
        patient_ipd.save()                     
        return redirect('/ipd')                  

    else:
        print('invalid')            
    context = {
        'patient_ipd': patient_ipd 
    }
    return render(request,'hmsapp/ipd_update.html',context)


def medicineUpdate(request,id):
    patient=Medicine_register.objects.get(id=id) 
    if request.method == 'POST': 
        medicine_name=request.POST['medicine_name']
        comapny_name=request.POST['comapny_name']
        medicine_category=request.POST['medicine_category']
        medicine_group=request.POST['medicine_group']
        pack=request.POST['pack']
        unit_pack=request.POST['unit_pack']
        patient.medicine_name = medicine_name
        patient.comapny_name = comapny_name 
        patient.medicine_category = medicine_category
        patient.medicine_group = medicine_group
        patient.pack = pack
        patient.unit_pack = unit_pack
        patient.save()
        return redirect('/pharmacy') 
    else:
        print('invalid') 
    
    context={'patient':patient}        
    return render(request,'hmsapp/update_medicine.html',context)

def pathologyView(request): 
     return render(request,'hmsapp/test_register.html')

def testView(request): 
    test= TestRegister.objects.all()   
    patients= Patient.objects.all()   
    doctor= Doctor.objects.all()   
    if request.method == "POST":  
        patient_name=request.POST['patient_name'] 
        blood_group=request.POST['blood_group'] 
        department=request.POST['department']  
        doctor = request.POST['doctor'] 
        testcase =request.POST['testcase'] 
        fees=request.POST['fees'] 
        pathology=TestRegister(patient_name=patient_name,blood_group=blood_group,department=department,doctor=doctor,testcase=testcase,fees=fees)
        pathology.save() 
        return redirect('/pathology')
    print(patients)                    
    context={'test':test,'patients':patients,'doctor':doctor} 
    return render(request,'hmsapp/test_register.html',context)

def testUpdateView(request,id): 
    test = TestRegister.objects.get(id=id) 
    if request.method == 'POST' : 
        print(test) 
        patient_name= request.POST['patient_name']   
        blood_group= request.POST['blood_group']   
        department= request.POST['department']    
        doctor = request.POST['doctor'] 
        testcase = request.POST['testcase'] 
        test.patient_name= patient_name 
        test.blood_group= blood_group 
        test.department= department 
        test.doctor= doctor  
        test.testcase= testcase  
        test.save() 
        print(test)       
        return redirect('/pathology') 
    else:
        print('invalid')    
                                                                             
    return render(request,'hmsapp/test_update.html',{'test':test}) 