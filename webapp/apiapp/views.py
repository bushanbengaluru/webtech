from django.shortcuts import render
from firstapp.models import Employee  # Import the Employee model if needed
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import EmpSerializer


@api_view(['GET'])
# Create your views here.
def getemployeeapi(request):
    if request.method == "GET":
        # Logic to retrieve employee data from the database
        emps = Employee.objects.all()
        # Serialize the employee data
        serializer = EmpSerializer(emps, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return render(request, "apiapp/error.html", {"error": "Invalid request method"})