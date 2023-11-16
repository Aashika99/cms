from django.urls import path
from .views import Patient_list,Patient_details_view,Doctor_Availability_view,\
    Doctor_Availability_details_view,Appointment_view,Appointment_details_view,\
    Appointment_bill_view,Appointment_bill_details_view,Medicine_list,Medicine_details_view,\
    Test_list,Test_details_view,LoginAPIView,LogoutAPIView, staff_list, staff_details_view, doctor_list, doctor_details_view


urlpatterns = [
    path('api/patient_details', Patient_list),
    path('api/patient_details/<int:passed_id>', Patient_details_view),
    path('api/doctor_availability', Doctor_Availability_view),
    path('api/doctor_availability/<int:passed_id>',Doctor_Availability_details_view),
    path('api/appointment', Appointment_view),
    path('api/appointment/<int:passed_id>',Appointment_details_view),
    path('api/appointment_bill', Appointment_bill_view),
    path('api/appointment_bill/<int:passed_id>', Appointment_bill_details_view),

    path('api/medicine', Medicine_list),
    path('api/medicine/<int:passed_id>',Medicine_details_view),
    path('api/test', Test_list),
    path('api/test/<int:passed_id>', Test_details_view),

    #akalya
    path('api/user/login', LoginAPIView.as_view(), name = 'user-login'),
    path('api/logout', LogoutAPIView.as_view(), name='logout'),
    path('api/staff', staff_list),
    path('api/staff/<int:passed_id>', staff_details_view),
    path('api/doctor', doctor_list ),
    path('api/doctor/<int:passed_id>', doctor_details_view ),



]
