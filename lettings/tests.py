"""
Tests for lettings app.

This module contains tests for models, views, and URLs of the lettings application.
"""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    """Test cases for the Address model."""

    def test_address_creation(self):
        """Test creating an address instance."""
        address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Springfield',
            state='IL',
            zip_code=62701,
            country_iso_code='USA'
        )
        assert address.number == 123
        assert address.street == 'Main Street'
        assert str(address) == '123 Main Street'

    def test_address_str_representation(self):
        """Test the string representation of an address."""
        address = Address.objects.create(
            number=456,
            street='Oak Avenue',
            city='Portland',
            state='OR',
            zip_code=97201,
            country_iso_code='USA'
        )
        assert str(address) == '456 Oak Avenue'


@pytest.mark.django_db
class TestLettingModel:
    """Test cases for the Letting model."""

    def test_letting_creation(self):
        """Test creating a letting instance with an address."""
        address = Address.objects.create(
            number=789,
            street='Beach Road',
            city='Miami',
            state='FL',
            zip_code=33101,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(
            title='Oceanview Condo',
            address=address
        )
        assert letting.title == 'Oceanview Condo'
        assert letting.address == address
        assert str(letting) == 'Oceanview Condo'


@pytest.mark.django_db
class TestLettingsViews:
    """Test cases for lettings views."""

    def test_lettings_index_view(self, client):
        """Test the lettings index view displays correctly."""
        response = client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert 'lettings/index.html' in [t.name for t in response.templates]

    def test_lettings_index_with_lettings(self, client):
        """Test lettings index shows lettings when they exist."""
        address = Address.objects.create(
            number=100,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        letting = Letting.objects.create(title='Test Letting', address=address)
        response = client.get(reverse('lettings:index'))
        assert letting.title.encode() in response.content

    def test_letting_detail_view(self, client):
        """Test individual letting detail view."""
        address = Address.objects.create(
            number=200,
            street='Detail Street',
            city='Detail City',
            state='DT',
            zip_code=54321,
            country_iso_code='DET'
        )
        letting = Letting.objects.create(title='Detail Letting', address=address)
        response = client.get(reverse('lettings:letting', kwargs={'letting_id': letting.id}))
        assert response.status_code == 200
        assert letting.title.encode() in response.content
        assert address.street.encode() in response.content


@pytest.mark.django_db
class TestLettingsURLs:
    """Test cases for lettings URL patterns."""

    def test_lettings_index_url_resolves(self, client):
        """Test that lettings index URL resolves correctly."""
        url = reverse('lettings:index')
        assert url == '/lettings/'
        response = client.get(url)
        assert response.status_code == 200

    def test_letting_detail_url_resolves(self, client):
        """Test that letting detail URL resolves correctly."""
        address = Address.objects.create(
            number=300,
            street='URL Street',
            city='URL City',
            state='UR',
            zip_code=99999,
            country_iso_code='URL'
        )
        letting = Letting.objects.create(title='URL Letting', address=address)
        url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        assert url == f'/lettings/{letting.id}/'
        response = client.get(url)
        assert response.status_code == 200
