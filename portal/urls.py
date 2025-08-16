"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from hub.views import (
    PortalLoginView,
    google_callback,
    google_login,
    microsoft_callback,
    microsoft_login,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", PortalLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("auth/microsoft/", microsoft_login, name="microsoft-login"),
    path(
        "auth/microsoft/callback/",
        microsoft_callback,
        name="microsoft-callback",
    ),
    path("auth/google/", google_login, name="google-login"),
    path("auth/google/callback/", google_callback, name="google-callback"),
    path("", include("hub.urls", namespace="hub")),
]
