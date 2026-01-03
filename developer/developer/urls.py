"""
https://docs.djangoproject.com/en/6.0/topics/http/urls/

Examples:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),

    path("", include("sso_miante.urls")),
    path("", include("sso_miante_client.urls")),
]
