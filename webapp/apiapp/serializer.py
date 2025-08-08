from rest_framework.serializers import ModelSerializer
from firstapp.models import Employee

class EmpSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"