from django.urls import path
from . import views


urlpatterns = [
    path("getemployee/", views.getemployeeapi),  # Include URLs from firstapp
]