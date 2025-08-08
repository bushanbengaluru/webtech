from django.urls import path
from . import views

urlpatterns = [
    path("addition/", views.formadd),  # Include URLs from formapp
]