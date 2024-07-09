import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from tasks.models import User


@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse('register')
    data = {
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_obtain_token():
    client = APIClient()
    url = reverse('token_obtain_pair')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_admin_user_creation():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpassword'
    )
    assert User.objects.filter(username='admin').exists()


@pytest.mark.django_db
def test_standard_user_creation():
    User.objects.create_user(
        username='standarduser',
        email='standarduser@example.com',
        password='standardpassword'
    )
    assert User.objects.filter(username='standarduser').exists()
