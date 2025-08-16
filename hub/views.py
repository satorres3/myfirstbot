from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

import msal
from google_auth_oauthlib.flow import Flow

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


def microsoft_login(request):
    app = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET,
    )
    auth_url = app.get_authorization_request_url(
        ["User.Read"], redirect_uri=settings.MICROSOFT_REDIRECT_URI
    )
    return redirect(auth_url)


def microsoft_callback(request):
    code = request.GET.get("code")
    if not code:
        return HttpResponse("No code provided", status=400)
    app = msal.ConfidentialClientApplication(
        settings.MICROSOFT_CLIENT_ID,
        authority=settings.MICROSOFT_AUTHORITY,
        client_credential=settings.MICROSOFT_CLIENT_SECRET,
    )
    result = app.acquire_token_by_authorization_code(
        code,
        scopes=["User.Read"],
        redirect_uri=settings.MICROSOFT_REDIRECT_URI,
    )
    return HttpResponse(result)


def google_login(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
    )
    auth_url, state = flow.authorization_url(
        prompt="consent", include_granted_scopes="true"
    )
    request.session["google_oauth_state"] = state
    return redirect(auth_url)


def google_callback(request):
    state = request.session.pop("google_oauth_state", "")
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
        state=state,
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
    )
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    creds = flow.credentials
    return HttpResponse(f"Google token: {creds.token}")
