from django.shortcuts import render

# Create your views here.
def insertview(request):
    if request.method == "GET":
        return render(request, "doctor/doctor.html")
