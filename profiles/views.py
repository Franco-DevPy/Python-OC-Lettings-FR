"""
Profiles views module.

This module contains the view functions for displaying user profiles.
"""
import logging
from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template with the list of all profiles.
    """
    logger.info("Profiles index requested")
    profiles_list = Profile.objects.all()
    logger.debug(f"{profiles_list.count()} profiles found")
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display details of a specific user profile.

    Args:
        request: HTTP request object.
        username: Username of the profile to display.

    Returns:
        Rendered template with the profile details.
    """
    logger.info(f"Profile detail requested: username='{username}'")
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile found: '{username}'")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)

    except Profile.DoesNotExist as e:
        logger.warning(f"Profile not found: username='{username}'")
        capture_exception(e)
        return render(request, 'profiles/profile.html', {
            'error': f"Profile '{username}' not found."
        })
    except Exception as e:
        logger.error(f"Unexpected error for profile '{username}': {e}", exc_info=True)
        capture_exception(e)
        raise