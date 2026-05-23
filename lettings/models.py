"""
Lettings models module.

This module contains the data models for managing rental properties
and their associated addresses.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing a physical address.

    Attributes:
        number: Street number (maximum 9999).
        street: Street name (maximum 64 characters).
        city: City name (maximum 64 characters).
        state: Two-letter state code.
        zip_code: ZIP code (maximum 99999).
        country_iso_code: Three-letter ISO country code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """Return string representation of the address."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model representing a rental property listing.

    Attributes:
        title: Title of the rental listing (maximum 256 characters).
        address: One-to-one relationship with the Address model.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the letting."""
        return self.title
