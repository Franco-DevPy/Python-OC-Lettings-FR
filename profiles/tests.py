"""
Tests for profiles app.

This module contains tests for models, views, and URLs of the profiles application.
"""
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
class TestProfileModel:
    """Test cases for the Profile model."""

    def test_profile_creation(self):
        """Test creating a profile instance."""
        user = User.objects.create_user(username='testuser', password='testpass123')
        profile = Profile.objects.create(user=user, favorite_city='Paris')
        assert profile.user.username == 'testuser'
        assert profile.favorite_city == 'Paris'
        assert str(profile) == 'testuser'

    def test_profile_str_representation(self):
        """Test the string representation of a profile."""
        user = User.objects.create_user(username='john_doe', password='pass123')
        profile = Profile.objects.create(user=user, favorite_city='London')
        assert str(profile) == 'john_doe'

    def test_profile_without_favorite_city(self):
        """Test profile can be created without favorite city."""
        user = User.objects.create_user(username='jane_doe', password='pass456')
        profile = Profile.objects.create(user=user)
        assert profile.favorite_city == ''


@pytest.mark.django_db
class TestProfilesViews:
    """Test cases for profiles views."""

    def test_profiles_index_view(self, client):
        """Test the profiles index view displays correctly."""
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert 'profiles/index.html' in [t.name for t in response.templates]

    def test_profiles_index_with_profiles(self, client):
        """Test profiles index shows profiles when they exist."""
        user = User.objects.create_user(username='testuser2', password='testpass')
        Profile.objects.create(user=user, favorite_city='Tokyo')
        response = client.get(reverse('profiles:index'))
        assert user.username.encode() in response.content

    def test_profile_detail_view(self, client):
        """Test individual profile detail view."""
        user = User.objects.create_user(
            username='detailuser',
            password='pass789',
            first_name='John',
            last_name='Smith',
            email='john@example.com'
        )
        profile = Profile.objects.create(user=user, favorite_city='New York')
        response = client.get(reverse('profiles:profile', kwargs={'username': user.username}))
        assert response.status_code == 200
        assert user.username.encode() in response.content
        assert profile.favorite_city.encode() in response.content


@pytest.mark.django_db
class TestProfilesURLs:
    """Test cases for profiles URL patterns."""

    def test_profiles_index_url_resolves(self, client):
        """Test that profiles index URL resolves correctly."""
        url = reverse('profiles:index')
        assert url == '/profiles/'
        response = client.get(url)
        assert response.status_code == 200

    def test_profile_detail_url_resolves(self, client):
        """Test that profile detail URL resolves correctly."""
        user = User.objects.create_user(username='urluser', password='urlpass')
        Profile.objects.create(user=user, favorite_city='Berlin')
        url = reverse('profiles:profile', kwargs={'username': user.username})
        assert url == f'/profiles/{user.username}/'
        response = client.get(url)
        assert response.status_code == 200
