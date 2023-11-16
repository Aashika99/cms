from django.shortcuts import render
from .models import Staff, Doctor, Medicine, MedicineBill, MedicineHistory, MedicineHistoryDetail, AppointmentBill, Appointment, LoginDetails, DoctorAvailability
from .models import Patient, Test
from .serializers import PatientSerializers, AppointmentSerializers, AppointmentBillSerializers, MedicineSerializers, MedicineHistorySerializers, MedicineBillSerializers, MedicineHistorydetailSerializers
from .serializers import DoctorSerializer, DoctorAvalabilitySerializers, StaffSerializer, TestSerializers,LoginSerializer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


# Create your views here.
class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log login details
                login_details, created = LoginDetails.objects.get_or_create(user=user)
                login_details.log_login()

                # Generate and return token
                token = Token.objects.get(user=user)
                response = {'username': username, 'status': status.HTTP_200_OK, 'message': 'success',
                            'data': {'Token': token.key}}
                return Response(response, status=status.HTTP_200_OK)

            else:
                response = {'status': status.HTTP_401_UNAUTHORIZED, 'message': 'Invalid username or password'}
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        response = {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Bad request', 'data': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):

    def post(self, request):
        user = request.user

        if user.is_authenticated:
            # Log the logout time
            try:
                login_details = LoginDetails.objects.get(user=user)
                login_details.log_logout()
            except LoginDetails.DoesNotExist:
                pass

            # Perform logout
            logout(request)
            response = {'status': status.HTTP_200_OK, 'message': 'Logout successful'}
            return Response(response, status=status.HTTP_200_OK)

        response = {'status': status.HTTP_401_UNAUTHORIZED, 'message': 'User not authenticated'}
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def Patient_list(request):
    if request.method == 'GET':
        patient_list = Patient.objects.all()
        serialize_Patient_list = PatientSerializers(patient_list, many=True)
        return JsonResponse(serialize_Patient_list.data, safe=False, status= 200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        patient_add_serializer = PatientSerializers(data=request_data)
        if patient_add_serializer.is_valid():
            patient_add_serializer.save()
            return JsonResponse(patient_add_serializer.data, status=201)

        return JsonResponse(patient_add_serializer.errors, status=400)

@csrf_exempt
def Patient_details_view(request, passed_id):
    patient_details = Patient.objects.get(id=passed_id)
    if request.method == 'GET':
        serialize_patient_details_list = PatientSerializers(patient_details)
        return JsonResponse(serialize_patient_details_list.data, safe=False, status=200)
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        patient_edit_serializer = PatientSerializers(patient_details, data=request_data)
        if patient_edit_serializer.is_valid():
            patient_edit_serializer.save()
            return JsonResponse(patient_edit_serializer.data, status=200)
        else:
            return JsonResponse(patient_edit_serializer.errors, status=400)
    elif request.method == 'DELETE':
        patient_details.delete()
        return HttpResponse(status=204)



@csrf_exempt
def Doctor_Availability_view(request):
    if request.method == 'GET':
        doctor_availability = DoctorAvailability.objects.all()
        serialize_doctor_availability = DoctorAvalabilitySerializers(doctor_availability, many=True)
        return JsonResponse(serialize_doctor_availability.data, safe=False, status= 200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        doctor_availability_add_serializer =  DoctorAvalabilitySerializers(data=request_data)
        if doctor_availability_add_serializer.is_valid():
            doctor_availability_add_serializer.save()
            return JsonResponse(doctor_availability_add_serializer.data, status=201)

        return JsonResponse(doctor_availability_add_serializer.errors, status=400)



@csrf_exempt
def Doctor_Availability_details_view(request, passed_id):
    doctor_availability = DoctorAvailability.objects.get(id=passed_id)
    if request.method == 'GET':
        serialize_doctor_availability = DoctorAvalabilitySerializers(doctor_availability)
        return JsonResponse(serialize_doctor_availability.data, safe=False, status=200)
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        doctor_availability_edit_serializer = DoctorAvalabilitySerializers(doctor_availability, data=request_data)
        if doctor_availability_edit_serializer.is_valid():
            doctor_availability_edit_serializer.save()
            return JsonResponse(doctor_availability_edit_serializer.data, status=200)
        else:
            return JsonResponse(doctor_availability_edit_serializer.errors, status=400)
    elif request.method == 'DELETE':
        doctor_availability.delete()
        return HttpResponse(status=204)



@csrf_exempt
def Appointment_view(request):
    if request.method == 'GET':
        appointment_list = Appointment.objects.all()
        serialize_appointment_list = AppointmentSerializers(appointment_list, many=True)
        return JsonResponse(serialize_appointment_list.data, safe=False, status= 200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        appointment_list_add_serializer =  AppointmentSerializers(data=request_data)
        if appointment_list_add_serializer.is_valid():
            appointment_list_add_serializer.save()
            return JsonResponse(appointment_list_add_serializer.data, status=201)

        return JsonResponse(appointment_list_add_serializer.errors, status=400)

@csrf_exempt
def Appointment_details_view(request, passed_id):
    appointment_list_view = Appointment.objects.get(id=passed_id)
    if request.method == 'GET':
        serialize_appointment_list_view = AppointmentSerializers(appointment_list_view)
        return JsonResponse(serialize_appointment_list_view.data, safe=False, status=200)
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        appointment_list_view_edit_serializer = AppointmentSerializers(appointment_list_view, data=request_data)
        if appointment_list_view_edit_serializer.is_valid():
            appointment_list_view.save()
            return JsonResponse(appointment_list_view_edit_serializer.data, status=200)
        else:
            return JsonResponse(appointment_list_view_edit_serializer.errors, status=400)
    elif request.method == 'DELETE':
        appointment_list_view.delete()
        return HttpResponse(status=204)


@csrf_exempt
def Appointment_bill_view(request):
    if request.method == 'GET':
        appointment_bill = AppointmentBill.objects.all()
        serialize_appointment_bill= AppointmentBillSerializers(appointment_bill, many=True)
        return JsonResponse(serialize_appointment_bill.data, safe=False, status= 200)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        appointment_bill_add_serializer =  AppointmentBillSerializers(data=request_data)
        if appointment_bill_add_serializer.is_valid():
            appointment_bill_add_serializer.save()
            return JsonResponse(appointment_bill_add_serializer.data, status=201)
        return JsonResponse(appointment_bill_add_serializer.errors, status=400)


@csrf_exempt
def Appointment_bill_details_view(request, passed_id):
    appointment_bill = AppointmentBill.objects.get(id=passed_id)
    if request.method == 'GET':
        serialize_appointment_bill = AppointmentBillSerializers(appointment_bill)
        return JsonResponse(serialize_appointment_bill.data, safe=False, status=200)
    elif request.method == 'PUT':
        request_data = JSONParser().parse(request)
        appointment_bill_edit_serializer = AppointmentBillSerializers(appointment_bill, data=request_data)
        if appointment_bill_edit_serializer.is_valid():
            appointment_bill_edit_serializer.save()
            return JsonResponse(appointment_bill_edit_serializer.data, status=200)
        else:
            return JsonResponse(appointment_bill_edit_serializer.errors, status=400)
    elif request.method == 'DELETE':
        appointment_bill.delete()
        return HttpResponse(status=204)


@csrf_exempt
def Test_list(request):
    try:
        if request.method == 'GET':
            test_list = Test.objects.all()
            serialize_test_list = TestSerializers(test_list, many=True)
            return JsonResponse(serialize_test_list.data, safe=False, status=200)
        elif request.method == 'POST':
            request_data = JSONParser().parse(request)
            test_add_serializer = TestSerializers(data=request_data)
            if test_add_serializer.is_valid():
                test_add_serializer.save()
                return JsonResponse(test_add_serializer.data, status=201)

            return JsonResponse(test_add_serializer.errors, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def Test_details_view(request, passed_id):
    try:
        test_details = Test.objects.get(id=passed_id)
        if request.method == 'GET':
            serialize_test_details_list = TestSerializers(test_details)
            return JsonResponse(serialize_test_details_list.data, safe=False, status=200)
        elif request.method == 'PUT':
            request_data = JSONParser().parse(request)
            test_edit_serializer = TestSerializers(test_details, data=request_data)
            if test_edit_serializer.is_valid():
                test_edit_serializer.save()
                return JsonResponse(test_edit_serializer.data, status=200)
            else:
                return JsonResponse(test_edit_serializer.errors, status=400)
        elif request.method == 'DELETE':
            test_details.delete()
            return HttpResponse(status=204)
    except Test.DoesNotExist:
        return JsonResponse({'error': 'Test not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def Medicine_list(request):
    try:
        if request.method == 'GET':
            medicine_list = Medicine.objects.all()
            serialize_medicine_list = MedicineSerializers(medicine_list, many=True)
            return JsonResponse(serialize_medicine_list.data, safe=False, status=200)
        elif request.method == 'POST':
            request_data = JSONParser().parse(request)
            medicine_add_serializer = MedicineSerializers(data=request_data)
            if medicine_add_serializer.is_valid():
                medicine_add_serializer.save()
                return JsonResponse(medicine_add_serializer.data, status=201)

            return JsonResponse(medicine_add_serializer.errors, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def Medicine_details_view(request, passed_id):
    try:
        medicine_details = Medicine.objects.get(id=passed_id)
        if request.method == 'GET':
            serialize_medicine_details_list = MedicineSerializers(medicine_details)
            return JsonResponse(serialize_medicine_details_list.data, safe=False, status=200)
        elif request.method == 'PUT':
            request_data = JSONParser().parse(request)
            medicine_edit_serializer = MedicineSerializers(medicine_details, data=request_data)
            if medicine_edit_serializer.is_valid():
                medicine_edit_serializer.save()
                return JsonResponse(medicine_edit_serializer.data, status=200)
            else:
                return JsonResponse(medicine_edit_serializer.errors, status=400)
        elif request.method == 'DELETE':
            medicine_details.delete()
            return HttpResponse(status=204)
    except Medicine.DoesNotExist:
        return JsonResponse({'error': 'Medicine not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


#akalya


@csrf_exempt
def staff_list(request):
    if request.method == "GET":
        # Fetch all the posts data and save it in a query set
        staff_list = Staff.objects.all()
        # seerialize the query set
        serialized_staff_list = StaffSerializer(staff_list, many=True)
        # return the serialized object as a json response
        # safe = false for json to accept dictionaries and other data types
        return JsonResponse(serialized_staff_list.data, safe=False, status=200)
    elif request.method == "POST":
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using serializer serialize the parsed json
        staff_add_serializer = StaffSerializer(data=request_data)
        # if the serializer returned a valid serialized data
        if staff_add_serializer.is_valid():
            staff_add_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(staff_add_serializer.data, status=201)
        return JsonResponse(staff_add_serializer.errors, status=400)

@csrf_exempt
def staff_details_view(request, passed_id):
    try:
        staff_details = Staff.objects.get(id=passed_id)
    except Staff.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serialized_staff_details = StaffSerializer(staff_details)
        return JsonResponse(serialized_staff_details.data, safe=False, status=200)

    elif request.method == "PUT":
        request_data = JSONParser().parse(request)
        staff_edit_serializer = StaffSerializer(staff_details, data=request_data)

        if staff_edit_serializer.is_valid():
            staff_edit_serializer.save()
            return JsonResponse(staff_edit_serializer.data, status=200)
        return JsonResponse(staff_edit_serializer.errors, status=400)

    elif request.method == "DELETE":
        # Instead of deleting, set is_active to False
        staff_details.is_active = False
        staff_details.save()
        return HttpResponse(status=204)  # Disable was successful


@csrf_exempt
def doctor_list(request):
    if request.method == "GET":
        # Fetch all the posts data and save it in a query set
        doctor_list = Doctor.objects.all()
        # serialize the query set
        serialized_doctor_list = DoctorSerializer(doctor_list, many=True)
        # return the serialized object as a json response
        # safe = false for json to accept dictionaries and other data types
        return JsonResponse(serialized_doctor_list.data, safe=False, status=200)
    elif request.method == "POST":
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using serializer serialize the parsed json
        doctor_add_serializer = DoctorSerializer(data=request_data)
        # if the serializer returned a valid serialized data
        if doctor_add_serializer.is_valid():
            doctor_add_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(doctor_add_serializer.data, status=201)
        return JsonResponse(doctor_add_serializer.errors, status=400)

@csrf_exempt
def doctor_details_view(request, passed_id):
    try:
        doctor_details = Doctor.objects.get(doctor_id=passed_id)
    except Doctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serialized_doctor_details = DoctorSerializer(doctor_details)
        return JsonResponse(serialized_doctor_details.data, safe=False, status=200)

    elif request.method == "PUT":
        request_data = JSONParser().parse(request)
        doctor_edit_serializer = DoctorSerializer(doctor_details, data=request_data)

        if doctor_edit_serializer.is_valid():
            doctor_edit_serializer.save()
            return JsonResponse(doctor_edit_serializer.data, status=200)
        return JsonResponse(doctor_edit_serializer.errors, status=400)

    elif request.method == "DELETE":
        # Instead of deleting, set is_active to False
        doctor_details.is_active = False
        doctor_details.save()
        return HttpResponse(status=204)
