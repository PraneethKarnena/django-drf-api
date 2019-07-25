from django.urls import path
from . import views

urlpatterns = [
    path('isd/', views.insert_sample_data)
]

