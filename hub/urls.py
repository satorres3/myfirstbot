from django.urls import path
from .views import DepartmentListView, DepartmentCreateView

app_name = "hub"

urlpatterns = [
    path("", DepartmentListView.as_view(), name="dashboard"),
    path("departments/new/", DepartmentCreateView.as_view(), name="department-create"),
]
