"""
Profiles admin configuration module.

This module configures the Django admin interface for profiles.
"""
from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model.

    Attributes:
        list_display: Fields to display in the admin list view.
    """

    list_display = ('user', 'favorite_city')


admin.site.register(Profile, ProfileAdmin)
