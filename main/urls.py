from django.urls import path,include
from . import views  
# from .views import autosuggest
urlpatterns = [ 
    # path("", views.index, name="index"), 
    path("", views.dashboard, name="dashboard"), 
    path("login/", views.login, name="login"), 
    path('logout/', views.logout, name='logout'), 
    path("add_patient/", views.add_patient, name="add_patient"), 
    path("patient_list/", views.patient_list, name="patient_list"), 
    path('patientdetails/',views.patientDetailsView),  
    path("patient/<str:pk>", views.patient, name="patient"),
    path('patientdetailsid/<int:id>', views.patient_details_id), 
    path("autosuggest/", views.autosuggest, name="autosuggest"),  
    path("autodoctor/", views.autodoctor, name="autodoctor"), 
    path("info/", views.info, name="info"),    
    path('profile/',views.profile),           
    path('deletepatient/<int:id>',views.delete_patient),  
    path('opd/',views.opdView),  
    path('opddetails/<int:id>',views.opd_details_id),  
    path('opddelete/<int:id>',views.opd_deleteView), 
    path('ipddelete/<int:id>',views.ipd_deleteView), 
    path('delete_medicine/<int:id>',views.pharmacy_deleteView),  
    path('ipd/',views.ipdView), 
    path('pharmacy/',views.pharmacyView), 
    path('pathology/',views.pathologyView),  
    path('medicinedetails/<int:id>',views.medicineDetailsById), 
    path('bed/',views.bedsView), 
    path('billing/',views.billingView),
    path('payment/',views.paymentView),
    path('successpayment',views.successPayment),
    path('beddetails/<str:bed_num>',views.bedDetailsView), 
    path('testdetails/<int:id>',views.testDetailsView),
    path('testdelete/<int:id>',views.testDeleteView),
    path('alltestcase/<str:testcase>',views.pathologyDetailsListView),
    path('',include('hmsapp.urls')), 
    path('billpage/',views.totalbill)
] 
 

