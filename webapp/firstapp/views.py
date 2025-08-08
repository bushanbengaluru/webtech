from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Employee  # Import the Employee model if needed
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def firstview(request):
    # return HttpResponse("Hello world")
    if request.method == "GET":
        return render(request, "firstapp/add.html", {"name": "Django"})
    elif request.method == "POST":
        v1 = request.POST['t1']
        v2 = request.POST['t2']
        try:
            result = int(v1) + int(v2)
            name = f"Result is {result}"
        except ValueError:
            name = "Please enter valid integers"
        return render(request, "firstapp/add.html", {"result": result})
def insertview(request):
    if request.method == "GET":
        return render(request, "firstapp/insert.html")
    elif request.method == "POST":
        eid = (request.POST['eid'])
        ename = request.POST['ename']
        esal = (request.POST['esal'])
        try:
            emps = Employee.objects.create(eid=eid, ename=ename, esal=esal)
        except ValueError:
            name = "Please enter valid data"
        return render(request, "firstapp/insert.html", {"msg": "Data Inserted Successfully"})

def recordview(request):
    if request.method == "GET":
        emps = Employee.objects.all()  # Fetch all employee records
        return render(request, "firstapp/select.html", {"employees": emps})  # Pass the records to the template
    elif request.method == "POST":
        minsal = int(request.POST['minsal'])
        maxsal = int(request.POST['maxsal'])
        emps = Employee.objects.filter(esal__range=(minsal, maxsal))  # variable is esal, salary range Syntax is __range (SELECT * FROM employee WHERE esal BETWEEN minsal AND maxsal)
        return render(request, "firstapp/select.html", {"employees": emps, "minsal": minsal, "maxsal": maxsal})

def updateemp(request, eid):
    if request.method == "GET":
        eb = Employee.objects.get(eid=eid)  # Fetch the employee record by eid
        # return HttpResponse("update employee emp")
        return render(request, "firstapp/update.html", {"employees": eb})  # Pass the employee data to the template
    elif request.method == "POST":
        eid=int(request.POST['eid'])
        ename = request.POST['ename']
        esal = int(request.POST['esal'])
        ebjs = Employee.objects.filter(eid=eid).update(eid=eid,ename=ename,esal=esal)  # Filter the employee record by eid
        return render(request,'firstapp/update.html')

def deleteemp(request, eid):
    if request.method == "GET":
        eb = Employee.objects.get(eid=eid)  # Fetch the employee record by eid
        return render(request, "firstapp/delete.html", {"employees": eb})  # Pass the employee data to the template
    elif request.method == "POST":
        Employee.objects.filter(eid=eid).delete()  # Delete the employee record by eid
        return redirect('selecturl')  # Redirect to the employee list or another view after deletion
    return HttpResponse("Invalid request method for delete operation")

def loginpage(request):
    if request.method == "GET":
        return render(request, "firstapp/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        valid_user = authenticate(request, username=username,password=password)  # Initialize valid_user to None
        # Here you would typically authenticate the user
        if valid_user == 'None':
            return render(request, "firstapp/login.html", {"error": "Invalid credentials"})
        else:
            return redirect('selecturl')  # Redirect to the employee list after successful login

    
def signuppage(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "firstapp/signup.html", {"form": form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginurl')  # Redirect to the login page after successful signup
        else:
            return render(request, "firstapp/signup.html", {"form": form})