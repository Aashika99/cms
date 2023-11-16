from django.contrib import admin
from .models import Doctor,Staff,Patient,DoctorAvailability,Appointment,AppointmentBill,Medicine,Test,MedicineHistory,MedicineHistoryDetail,MedicineBill,LabBill,LabReport
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Patient)
admin.site.register(DoctorAvailability)
admin.site.register(Appointment)
admin.site.register(AppointmentBill)
admin.site.register(Test)
admin.site.register(Medicine)
admin.site.register(MedicineHistory)
admin.site.register(MedicineHistoryDetail)
admin.site.register(MedicineBill)
admin.site.register(LabBill)
admin.site.register(LabReport)



