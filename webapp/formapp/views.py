from django.shortcuts import render

# Create your views here.
def formadd(request):
    if request.method == "GET":
        return render(request, "formapp/addition.html")
    elif request.method == "POST":
        v1 = request.POST['value1']
        v2 = request.POST['value2']
        try:
            result = int(v1) + int(v2)
            return render(request, "formapp/addition.html", {"result": result})
        except ValueError:
            return render(request, "formapp/addition.html", {"error": "Please enter valid integers"})