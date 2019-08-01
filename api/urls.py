from django.urls import path
from . import views

urlpatterns = [
    path('isd/', views.insert_sample_data),
    path('get-patients/', views.initial_patient_details),
    path('get-doctors/', views.doctors_details),
    path('send-request/<int:patient_id>/<int:doctor_id>/', views.send_request),
]

