from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DeleteView,UpdateView,DetailView
from employee_management.models import Employee,Position,Department
from django.urls import reverse_lazy
from employee_management.forms import Employee_Form
# Create your views here.

class HomePage(TemplateView):
    template_name="employee_management/base.html"
class EmployeeListView(ListView):
    context_object_name="emp_list"
    model=Employee
    template_name="employee_management/employee_list.html"
class EmployeeCreateView(CreateView):
    fields="__all__"
    # form_class=Employee_Form
    model=Employee
   
class EmployeeUpdateView(UpdateView):
    fields=("First_Name","Salary","Location","Phone_No")
    model=Employee
class EmployeeDeleteView(DeleteView):
    context_object_name="del_emp"
    model=Employee
    success_url=reverse_lazy("emp:view")
class EmployeeDetailView(DetailView):
    context_object_name='emp_detail'
    model=Employee


    
