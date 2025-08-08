from django.shortcuts import render

# Create your views here.
def patient(request):
    return render(request, 'clinic/patient.html')