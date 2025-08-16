from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Department
from .forms import DepartmentForm


class PortalLoginView(LoginView):
    template_name = "hub/login.html"


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "hub/dashboard.html"
    context_object_name = "departments"


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "hub/department_form.html"
    success_url = reverse_lazy("hub:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
