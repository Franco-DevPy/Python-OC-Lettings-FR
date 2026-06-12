"""
Main URL configuration for OC Lettings Site.

Includes URL patterns for the homepage, admin, and sub-applications.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


def trigger_error(request):
    """Test view to trigger a Sentry error for verification."""
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('sentry-debug/', trigger_error),
    ]
