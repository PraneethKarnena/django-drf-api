from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import models
from . import serializers


def home(request):
    return render(request, 'api/home.html')

def insert_sample_data(request):
    fake = Faker()
    for _ in range(10):
        _ = models.PatientModel.objects.create(
            name=fake.profile()['name'],
            email=fake.profile()['mail'],
            address=fake.profile()['address'],
            company=fake.profile()['company'],
            job=fake.profile()['job'],
            mobile=fake.phone_number(),
            dob=fake.profile()['birthdate'],
            blood_group=fake.profile()['blood_group'],
        )

    for _ in range(10):
        _ = models.DoctorModel.objects.create(
            name=fake.profile()['name'],
            email=fake.profile()['mail'],
        )

    return HttpResponse('Ok!')


@api_view(['GET'])
def initial_patient_details(request):
    patients = models.PatientModel.objects.all()
    patients_serializer = serializers.InitialPatientSerializer(patients, many=True)
    return Response(data={'data': patients_serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def doctors_details(request):
    doctors = models.DoctorModel.objects.all()
    doctors_serializer = serializers.DoctorsSerializer(doctors, many=True)
    return Response(data={'data': doctors_serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def send_request(request, patient_id, doctor_id):
    try:
        friendship = models.FriendModel.objects.get(patient_id=patient_id, doctor_id=doctor_id)
        return Response(data={'error': 'Already friends!'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        try:
            patient = models.PatientModel.objects.get(id=patient_id)
            doctor = models.DoctorModel.objects.get(id=doctor_id)
            friendship = models.FriendModel.objects.create()
            friendship.patient.add(patient)
            friendship.doctor.add(doctor)
            friendship.save()
            friends_serializer = serializers.FriendsSerializer(friendship, many=False)
            return Response(data={'data': friends_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def accept_request(request, patient_id, doctor_id, action):
    try:
        if action in ('ACCEPT', 'REJECT'):
            friendship = models.FriendModel.objects.get(patient__id=patient_id, doctor__id=doctor_id)
            print(friendship.patient)
            choices = {'ACCEPT': 'ACC', 'REJECT': 'REJ'}
            friendship.status = choices[action]
            friendship.save()
            friends_serializer = serializers.FriendsSerializer(friendship, many=False)
            return Response(data={'data': friends_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'Invalid Action!'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def patient_data(request, patient_id, doctor_id):
    try:
        _ = models.FriendModel.objects.get(patient__id=patient_id, doctor__id=doctor_id, status='ACC')
        patient = models.PatientModel.objects.get(id=patient_id)
        friendship_serializer = serializers.PatientSerializer(patient, many=False)
        return Response(data={'data': friendship_serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)