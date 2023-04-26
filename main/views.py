from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *  
from hmsapp.models import *
from .filters import PatientFilter
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# PatientFilter = OrderFilter

# Create your view

def login(request): 
    if request.user.is_authenticated:
        return redirect('/') 
    else:  
        if request.method == 'POST':
            username = request.POST['username']      
            password = request.POST['password']      
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')                                                                      
            else: 
                messages.error(request, 'Invalid username or password')
                return redirect('login')
        else:
            return render(request, 'main/login.html') 


@login_required(login_url='login')    
def logout(request): 
    auth.logout(request)     
    return redirect('/') 

def dashboard(request): 
    patients = Patient.objects.all() 
    patient_count = patients.count()  
    patients_recovered = Patient.objects.filter(status="Recovered")  
    patients_deceased = Patient.objects.filter(status="Deceased")  
    deceased_count = patients_deceased.count()     
    recovered_count = patients_recovered.count()   
    beds = Bed.objects.all()      
    beds_available = Bed.objects.filter(occupied=False).count()    
    context =  {   
        'patient_count': patient_count,
        'recovered_count': recovered_count,
        'beds_available': beds_available,
        'deceased_count':deceased_count, 
        'beds':beds 
    }        
    # print(patient_count) 
    return render(request, 'main/dashboard.html', context) 


def add_patient(request):
    beds = Bed.objects.filter(occupied=False)  
    doctors = Doctor.objects.all()   
    if request.method == "POST":      
        name = request.POST['name']     
        phone_num = request.POST['phone_num']      
        patient_relative_name = request.POST['patient_relative_name'] 
        patient_relative_contact = request.POST['patient_relative_contact']      
        address = request.POST['address']   
        symptoms = request.POST['symptoms'] 
        print(symptoms) 
        prior_ailments = request.POST['prior_ailments']
        bed_num_sent = request.POST['bed_num'] 
        bed_num = Bed.objects.get(bed_number=bed_num_sent) 
        dob = request.POST['dob']               
        status = request.POST['status']                            
        doctor = request.POST['doctor']                                    
        doctor = Doctor.objects.get(name=doctor)     
        fees = request.POST['fees'] 
        print(request.POST)   
        patient = Patient.objects.create(  
        name = name ,      
        phone_num = phone_num,  
        patient_relative_name = patient_relative_name,
        patient_relative_contact = patient_relative_contact, 
        address = address,   
        symptoms = symptoms,  
        prior_ailments = prior_ailments,  
        bed_num = bed_num,   
        dob = dob,  
        doctor=doctor,         
        status = status,
        fees=fees,   
        )  
        patient.save()  
        print(patient) 
        bed = Bed.objects.get(bed_number=bed_num_sent)
        bed.occupied = True 
        bed.save() 
        id = patient.id
        return redirect(f"/patient/{id}")
        
    context = {
        'beds': beds,
        'doctors': doctors
    } 
    return render(request, 'main/add_patient.html', context)
   
def patient(request, pk):
    patient = Patient.objects.get(id=pk)                     
    if request.method == "POST":                             
        doctor = request.POST['doctor'] 
        doctor_time = request.POST['doctor_time']
        doctor_notes = request.POST['doctor_notes'] 
        mobile = request.POST['mobile'] 
        mobile2 = request.POST['mobile2'] 
        relativeName = request.POST['relativeName'] 
        address  = request.POST['location'] 
        # print(doctor_time)                           
        # print(doctor_notes)                          
        status = request.POST['status']                         
        doctor = Doctor.objects.get(name=doctor)             
        # print(doctor) 
        patient.phone_num = mobile 
        patient.patient_relative_contact = mobile2
        patient.patient_relative_name = relativeName
        patient.address = address  
        patient.doctor = doctor    
        patient.doctors_visiting_time = doctor_time 
        patient.doctors_notes = doctor_notes 
        # print(patient.doctors_visiting_time) 
        # print(patient.doctors_notes) 
        patient.status = status  
        patient.save()  
        return redirect("/patient_list")  
    else:     
        print('invalid credential')      
    print(patient) 
    print(patient)   
    context = {  
        'patient': patient  
    } 
    return render(request, 'main/patient.html', context) 

def delete_patient(request,id):
    patient=Patient.objects.get(id=id) 
    patient.delete() 
    return render(request,'main/patient_details.html') 
 
def patient_details_id(request,id):
    patient = Patient.objects.get(id=id) 
    print(patient.symptoms ) 
    return render(request,'main/patient_id_details.html',{'patient':patient})


def patient_list(request): 
    patients = Patient.objects.all()
    # filtering 
    myFilter = PatientFilter(request.GET, queryset=patients) 
    
    patients = myFilter.qs 
    context = { 
        'patients': patients,
        'myFilter': myFilter
    } 
    return render(request, 'main/patient_list.html', context)

'''
def autocomplete(request):      
    if patient in request.GET:          
        name = Patient.objects.filter(name__icontains=request.GET.get(patient))
        name = ['js', 'python']                
        names = list()      
        names.append('Shyren')              
        print(names)
        for patient_name in name:       
            names.append(patient_name.name)      
        return JsonResponse(names, safe=False)       
    return render (request, 'main/patient_list.html')     
'''

def patientDetailsView(request):
    patients=Patient.objects.all()
    return render(request,'main/patient_details.html',{'patients':patients})   

def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = Patient.objects.filter(name__icontains=query_original)
    mylist = [] 
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def autodoctor(request): 
    query_original = request.GET.get('term')
    queryset = Doctor.objects.filter(name__icontains=query_original)
    mylist = [ ]                                  
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False) 

def info(request):   
    return render(request, "main/info.html")
  
def profile(request):
    return render(request,'main/profile.html')  

def opdView(request):
    patients=OpdRegister.objects.all()    
    return render(request,'main/opd.html',{'patients':patients}) 

def opd_deleteView(request,id): 
    patient=OpdRegister.objects.get(id=id) 
    patient.delete() 
    return render(request,'main/opd.html')    

def opd_details_id(request,id): 
    patient = OpdRegister.objects.get(id=id)  
    return render(request,'main/opd_details.html',{'patient':patient}) 

def ipdView(request):   
    patients=IpdRegister.objects.all() 
    return render(request,'main/ipd.html',{'patients':patients})

def ipd_deleteView(request,id):
    patient=IpdRegister.objects.get(id=id)
    patient.delete()
    return render(request,'main/ipd.html')

def pharmacyView(request):   
    medicine=Medicine_register.objects.all()        
    context={'medicine':medicine} 
    return render(request,'main/pharmacy.html',context)     
        
def medicineDetailsById(request,id):
    medicine=Medicine_register.objects.get(id=id)
    context={'medicine':medicine}              
    return render(request,'main/medicine_id_details.html',context)
                
def pharmacy_deleteView(request,id):
    patient=Medicine_register.objects.get(id=id)             
    patient.delete()                              
    return render(request,'main/pharmacy.html')            
                                    
def bedsView(request):     
    beds = Bed.objects.all()                
    return render(request,'main/bed.html',{'beds':beds})       
                                                           
def bedDetailsView(request,bed_num):                           
    patient=Patient.objects.get(bed_num=bed_num)                        
    return render(request,'main/bedstatus.html',{'patient':patient})            
                 
def pathologyView(request):  
    test= TestRegister.objects.all()    
    return render(request,'main/pathology.html',{'test':test})   
                                        
def testDetailsView(request,id):      
    test= TestRegister.objects.get(id=id)                
    patient1=IpdRegister.objects.get(id=id) 
    print(test.patient_name) 
    total= test.fees+patient1.fees 
    print(total) 
    return render(request,'main/test_details.html',{"test":test,'total':total,'patient1':patient1})      
                                                                             
def testDeleteView(request,id):                            
    test= TestRegister.objects.get(id=id) 
    test.delete()                       
    return render(request,'main/pathology.html')     

def pathologyDetailsListView(request,testcase):             
    Fever=TestRegister.objects.filter(testcase__iexact='fever')      
    Cough=TestRegister.objects.filter(testcase__iexact='cough')        
    Diabetes=TestRegister.objects.filter(testcase__iexact='diabetes') 
    Hemoglobin=TestRegister.objects.filter(testcase__iexact='hemoglobin') 
    Vitamin=TestRegister.objects.filter(testcase__iexact='vitamin')               
    Urin=TestRegister.objects.filter(testcase__iexact='urin')       
    Radiology=TestRegister.objects.filter(testcase__iexact='Radiology X-ray')  
    mri=TestRegister.objects.filter(testcase__iexact='MRI')                   
    print(mri)        
    # mri2=TestRegister.objects.get(testcase=testcase)                            
    print("************")                                                                     
    # print(mri2)                                                       
    Thyroid=TestRegister.objects.filter(testcase__iexact='thyroid')      
    context={"Fever": Fever,"Cough":Cough,"Diabetes":Diabetes,"Hemoglobin":Hemoglobin,"Vitamin":Vitamin,"Urin":Urin,"Radiology":Radiology,"mri":mri,"Thyroid":Thyroid}   
    return render(request,'main/mri.html',context)    

def testDetailsViewList(request):   
    return render(request,'main/loginadmin.html')             


def loginreceiptionist(request):  
    return render(request,'main/log')   

def billingView(request):
    patient=Patient.objects.all() 
    if request.method=='POST': 
        name=request.POST['name'] 
        email=request.POST['email'] 
        addr=request.POST['addr'] 
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip'] 
        bill=Bill.objects.create(name=name,email=email,addr=addr,city=city,state=state,zip=zip)
        bill.save()  
        return redirect('/payment')
    else:
        print('try again')    
   
    return render(request,'main/billing.html',{"patient":patient}) 


def paymentView(request):   
    if request.method=='POST': 
        amount=request.POST['amount'] 
        payment_mode=request.POST['payment_mode'] 
        # name_on_card=request.POST['name_on_card'] 
        # card_num=request.POST['card_num']   
        # exp_month=request.POST['exp_month'] 
        # exp_year=request.POST['exp_year'] 
        # cvv=request.POST['cvv']  
        payments=Payment.objects.create(amount=amount,payment_mode=payment_mode)
        payments.save() 
        print(payments) 
        return redirect('/successpayment')      

    else:
        print('please try again later')        
    return render(request,'main/payment.html') 

    
def successPayment(request): 
    return render(request,'main/payment_successful.html')    


def totalbill(request,str):
    patient=Patient.objects.get(str) 
    opd=OpdRegister.objects.get(id=id) 
    ipd=IpdRegister.objects.get(id=id) 
    pathology=TestRegister.objects.get(id=id) 
    pharmacy=Medicine_register.objects.get(id=id) 
    total= patient.fees+ ipd.fees+pathology.fees+pharmacy.rupees 
    print(total)  
    print(opd)      
    return render(request,'main/billpage.html') 
