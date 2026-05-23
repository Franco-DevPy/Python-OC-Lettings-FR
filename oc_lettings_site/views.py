"""
Main site views module.

This module contains the view for the homepage.
"""
from django.shortcuts import render


def index(request):
    """
    Display the homepage with navigation to lettings and profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered homepage template.
    """
    return render(request, 'index.html')
