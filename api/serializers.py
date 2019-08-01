from rest_framework import serializers
from . import models

class InitialPatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PatientModel
        fields = ['name', 'id']


class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DoctorModel
        fields = '__all__'