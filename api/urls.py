from django.urls import path
from . import views

urlpatterns = [
    path('isd/', views.insert_sample_data),
    path('get-patients/', views.initial_patient_details),
]

