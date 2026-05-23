"""
Profiles views module.

This module contains the view functions for displaying user profiles.
"""
from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Display a list of all user profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template with the list of all profiles.
    """
    profiles_list = Profile.objects.all()
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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
