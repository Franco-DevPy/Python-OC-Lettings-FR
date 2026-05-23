"""
Profiles models module.

This module contains the data model for user profiles.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile with additional information.

    Attributes:
        user: One-to-one relationship with Django's User model.
        favorite_city: User's favorite city (optional, maximum 64 characters).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return string representation of the profile."""
        return self.user.username
