from django.urls import path
from .views import DepartmentListView, DepartmentCreateView, PortalHomeView

app_name = "hub"

urlpatterns = [
    path("", DepartmentListView.as_view(), name="dashboard"),
    path("home/", PortalHomeView.as_view(), name="home"),
    path("departments/new/", DepartmentCreateView.as_view(), name="department-create"),
]
