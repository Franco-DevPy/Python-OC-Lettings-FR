"""
Lettings admin configuration module.

This module configures the Django admin interface for lettings models.
"""
from django.contrib import admin
from .models import Letting, Address


class AddressAdmin(admin.ModelAdmin):
    """
    Admin configuration for Address model.

    Attributes:
        list_display: Fields to display in the admin list view.
    """

    list_display = ('number', 'street', 'city', 'state', 'zip_code', 'country_iso_code')


admin.site.register(Address, AddressAdmin)
admin.site.register(Letting)
