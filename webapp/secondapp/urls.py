from django.urls import path
from.import views
urlpatterns = [
    path("", views.secondview)  # Include URLs from firstapp
]
