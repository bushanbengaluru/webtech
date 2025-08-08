from django.urls import path
from .import views
urlpatterns = [
    # path("", views.clinicview),  # Include URLs from firstapp
    path("patient/", views.patient, name='patienturl'),  # Include URLs from patient view
]
