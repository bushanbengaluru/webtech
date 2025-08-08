from django.urls import path
from .import views
urlpatterns = [
    #  path("clinic/", views.clinicview),  # Include URLs from firstapp
    path("", views.doctorview, name='doctorview'),  # Include URLs from doctor view
    path("doctor/", views.doctorview, name='doctorview'),  # Include URLs from doctor view
]
