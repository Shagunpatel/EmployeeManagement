from django.contrib import admin
from employee_management.models import Employee,Position,Department
# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Department)
