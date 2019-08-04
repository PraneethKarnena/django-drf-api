from django.db import models


class DoctorModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} - {self.email}'


class PatientModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    company = models.TextField()
    job = models.TextField()
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    blood_group = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.name} - {self.email}'


class FriendModel(models.Model):
    doctor = models.ManyToManyField(DoctorModel)
    patient = models.ManyToManyField(PatientModel)
    STATUS_CHOICES = (
        ('PEN', 'Pending'),
        ('ACC', 'Accepted'),
        ('REJ', 'Rejected'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')

    def __str__(self):
        return f'{str(self.doctor.name)} - {str(self.patient.name)} - {self.status}'