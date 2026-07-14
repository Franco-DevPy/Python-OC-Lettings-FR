"""
Tests for main OC Lettings Site.

This module contains tests for the homepage and main site functionality.
"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestHomepage:
    """Test cases for the main homepage."""

    def test_homepage_view(self, client):
        """Test that the homepage loads successfully."""
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assert 'index.html' in [t.name for t in response.templates]

    def test_homepage_content(self, client):
        """Test that homepage contains expected content."""
        response = client.get(reverse('index'))
        assert b'Welcome to Holiday Homes' in response.content

    def test_homepage_has_navigation_links(self, client):
        """Test that homepage has links to lettings and profiles."""
        response = client.get(reverse('index'))
        content = response.content.decode()
        assert 'lettings' in content.lower()
        assert 'profiles' in content.lower()


@pytest.mark.django_db
class TestMainURLs:
    """Test cases for main site URL patterns."""

    def test_index_url_resolves(self, client):
        """Test that the index URL resolves correctly."""
        url = reverse('index')
        assert url == '/'
        response = client.get(url)
        assert response.status_code == 200

    def test_admin_url_exists(self, client):
        """Test that admin URL is accessible."""
        response = client.get('/admin/')
        assert response.status_code == 302 or response.status_code == 200
