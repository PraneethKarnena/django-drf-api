from django.shortcuts import render
from django.http import HttpResponse
from . import models
from faker import Faker


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