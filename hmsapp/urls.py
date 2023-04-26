from django.urls import path
from hmsapp.views import *
 
urlpatterns = [     

    path('ipdregister/', ipdRegistrationView),    
    path('ipddetails/<int:id>',ipd_details_id), 
    path('ipdupdate/<int:id>',ipdUpdateView), 
    path('opdregister/',opd_RegisterView), 
    path('opdupdate/<int:id>',opdUpdateView),  
    path('medicineregister/',medicineRegisterView), 
    path('medicineupdate/<int:id>',medicineUpdate), 
    path('testregister/',testView), 
    path('testupdate/<int:id>',testUpdateView)  
    
] 