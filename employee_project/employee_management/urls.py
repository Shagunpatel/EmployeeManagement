from django.urls import path
from employee_management import views
app_name="emp"
urlpatterns = [
     path("",views.HomePage.as_view(),name="home"),
     path("view/",views.EmployeeListView.as_view(),name="view"),
     path("create/",views.EmployeeCreateView.as_view(),name="add"),
     path("update/<int:pk>/",views.EmployeeUpdateView.as_view(),name="update"),
     path("delete/<int:pk>/",views.EmployeeDeleteView.as_view(),name="delete"),
     path("detail<int:pk>/",views.EmployeeDetailView.as_view(),name="detail"),



]
