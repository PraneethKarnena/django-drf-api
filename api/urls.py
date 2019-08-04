from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('isd/', views.insert_sample_data),
    path('get-patients/', views.initial_patient_details),
    path('get-doctors/', views.doctors_details),
    path('send-request/<int:patient_id>/<int:doctor_id>/', views.send_request),
    path('request/<int:patient_id>/<int:doctor_id>/<slug:action>/', views.accept_request),
    path('view-patient/<int:patient_id>/<int:doctor_id>/', views.patient_data),
]

