"""
Lettings views module.

This module contains the view functions for displaying rental property
listings and their details.
"""
import logging
from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all available lettings.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template with the list of all lettings.
    """
    logger.info("Lettings index requested")
    lettings_list = Letting.objects.all()
    logger.debug(f"{lettings_list.count()} lettings found")
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
    logger.info(f"Letting detail requested: id={letting_id}")
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Letting found: '{letting.title}'")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)

    except Letting.DoesNotExist as e:
        logger.warning(f"Letting not found: id={letting_id}")
        capture_exception(e)
        return render(request, 'lettings/letting.html', {
            'error': f"Letting '{letting_id}' not found."
        })
    except Exception as e:
        logger.error(f"Unexpected error for letting id={letting_id}: {e}", exc_info=True)
        capture_exception(e)
        raise