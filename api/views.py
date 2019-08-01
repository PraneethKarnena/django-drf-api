from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import models
from . import serializers


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