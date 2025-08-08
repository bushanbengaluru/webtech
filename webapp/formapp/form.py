from django import forms

class addition(forms.Form):
    value1 = forms.IntegerField(label="Enter First Value")
    value2 = forms.IntegerField(label="Enter Second Value")
    # def __init__(self, name, age, salary):
    #     self.name = name
    #     self.age = age
    #     self.salary = salary

    # def display(self):
    #     return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"