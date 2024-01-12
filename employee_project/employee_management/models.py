from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    Department_Id=models.IntegerField(primary_key=True)
    Department_Name=models.CharField(max_length=256)
    Description=models.TextField()
    def __str__(self):
        return self.Department_Name

class Position(models.Model):
    Position_Id=models.IntegerField(primary_key=True)
    Position_Name=models.CharField(max_length=256)
    Description=models.TextField()
    def __str__(self):
        return self.Position_Name

class Employee(models.Model):
    Employee_Id=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=256)
    Last_Name=models.CharField(max_length=256)
    Salary=models.PositiveIntegerField()
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Position=models.ForeignKey(Position,on_delete=models.CASCADE)
    Location=models.CharField(max_length=256)
    Phone_No=models.BigIntegerField()
    Date_Of_Joining=models.DateField()

    def __str__(self):
        return self.First_Name
    

    def get_absolute_url(self):
        return reverse("emp:view")
    




