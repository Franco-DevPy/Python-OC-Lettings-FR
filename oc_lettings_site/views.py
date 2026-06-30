"""
Main site views module.

This module contains the view for the homepage.
"""
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)  # logger propre à ce module (oc_lettings_site.views)


def index(request):
    """
    Display the homepage with navigation to lettings and profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered homepage template.
    """
    logger.info("Homepage requested")
    return render(request, 'index.html')
