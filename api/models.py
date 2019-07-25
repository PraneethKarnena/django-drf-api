from django.db import models


class PatientModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    company = models.TextField()
    job = models.TextField()
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    blood_group = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name} - {self.email}'


class DoctorModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} - {self.email}'