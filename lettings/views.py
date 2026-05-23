"""
Lettings views module.

This module contains the view functions for displaying rental property
listings and their details.
"""
from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Display a list of all available lettings.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template with the list of all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display details of a specific letting.

    Args:
        request: HTTP request object.
        letting_id: ID of the letting to display.

    Returns:
        Rendered template with the letting details including title and address.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
