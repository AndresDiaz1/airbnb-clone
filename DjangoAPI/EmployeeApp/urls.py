from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path(r"^department/$", views.departmentAPI),
    path(r"^department/([0-9]+)$", views.departmentAPI),
]
