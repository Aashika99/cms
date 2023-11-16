from rest_framework import serializers
from .models import Staff, Doctor, Medicine, MedicineBill, MedicineHistory, MedicineHistoryDetail, AppointmentBill, \
    Appointment, LoginDetails, DoctorAvailability, LabBill, LabReport
from .models import Patient, Test
from django.contrib.auth.models import User



class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class MedicineBillSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicineBill
        fields = '__all__'


class MedicineHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicineHistory
        fields = '__all__'


class MedicineHistorydetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicineHistoryDetail
        fields = '__all__'


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']







class AppointmentSerializers(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.doctor.staff.name', read_only=True)
    patient_name = serializers.CharField(source='patient.fullname', read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorAvalabilitySerializers(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.staff.name',read_only=True)
    specialization = serializers.CharField(source='doctor.specialization',read_only=True)

    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class AppointmentBillSerializers(serializers.ModelSerializer):

    doctor_name = serializers.CharField(source='appointed_doc.doctor.staff.name', read_only=True)
    patient_name = serializers.CharField(source='patient.fullname', read_only=True)
    consultation_fee = serializers.CharField(source='appointed_doc.doctor.consultation_fee', read_only=True)


    class Meta:
        model = AppointmentBill
        fields = '__all__'


class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

#akalya
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        # providing the metadata to the ModelSerializer class
        model = Staff
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='staff.name', read_only=True)
    date_of_birth = serializers.CharField(source='staff.date_of_birth', read_only=True)
    age = serializers.CharField(source='staff.age', read_only=True)
    gender = serializers.CharField(source='staff.gender', read_only=True)
    role = serializers.CharField(source='staff.role', read_only=True)
    phone_number = serializers.CharField(source='staff.phone_number', read_only=True)
    date_of_joining = serializers.CharField(source='staff.date_of_joining', read_only=True)
    username = serializers.CharField(source='staff.username', read_only=True)
    password = serializers.CharField(source='staff.password', read_only=True)
    is_active = serializers.CharField(source='staff.is_active', read_only=True)

    class Meta:
        # providing the metadata to the ModelSerializer class
        model = Doctor
        fields = '__all__'



