from django.contrib import admin
from employee_management.models import Employee,Position,Department,Permission
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    fields=['Position_Name','Position_Id','Description']
    search_fields=['Position_Name','Position_Id','Description']
    list_filter=['Position_Name','Position_Id']
    list_display=['Position_Id','Position_Name']
    list_editable=['Position_Name']
admin.site.register(Employee)
# admin.site.register(Runner)
admin.site.register(Position,EmpAdmin)
admin.site.register(Department)
admin.site.register(Permission)

# admin.site.register(Pizza)
# admin.site.register(Topping)

