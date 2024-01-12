from django import forms
from employee_management.models import Employee

class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        