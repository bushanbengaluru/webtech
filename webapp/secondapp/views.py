from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def secondview(request):
    return HttpResponse("BYE")  # Render a template with context
    # return HttpResponse("Hello from second app")  # Alternatively, return a simple HTTP response