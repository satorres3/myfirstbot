from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

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


class PortalHomeView(TemplateView):
    template_name = "hub/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = [
            {
                "title": "The future of AI apps and agents starts here",
                "summary": "Explore how AI agents are reshaping the tech landscape.",
                "category": "Announcements",
                "date": "Aug 7, 2025",
                "read_time": 6,
                "image": "https://via.placeholder.com/800x400",
            },
            {
                "title": "Building secure multi-agent systems",
                "category": "Security",
                "date": "Jul 12, 2025",
                "read_time": 4,
                "image": "https://via.placeholder.com/400x200",
            },
            {
                "title": "Optimizing cloud costs with AI",
                "category": "Best Practices",
                "date": "Jun 30, 2025",
                "read_time": 5,
                "image": "https://via.placeholder.com/400x200",
            },
        ]
        return context
