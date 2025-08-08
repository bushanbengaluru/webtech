from django.urls import path
from .import views
urlpatterns = [
    path("", views.firstview),  # Include URLs from firstapp
    path("insert/", views.insertview),  # Include URLs from firstapp
    path("select/", views.recordview, name='selecturl'),  # Include URLs from firstapp
    path("update/<int:eid>", views.updateemp, name='employeeurl'),  # Update view URL
    path("delete/<int:eid>", views.deleteemp, name='deleteurl'),  # Delete view URL
    path('login/', views.loginpage, name='loginurl'),  # Login view URL
    path('signup/', views.signuppage, name='signurl'),  # Login view URL
]
