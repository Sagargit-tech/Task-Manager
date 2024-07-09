import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from tasks.models import User, Task


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    url = reverse('task-list')
    user = User.objects.create_user(
        username='standarduser',
        email='standarduser@example.com',
        password='standardpassword'
    )
    data = {
        'title': 'New Task',
        'description': 'Task description',
        'assigned_to': user.id
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_standard_user_permissions():
    client = APIClient()
    user = User.objects.create_user(
        username='standarduser',
        email='standarduser@example.com',
        password='standardpassword'
    )
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpassword'
    )

    task = Task.objects.create(
        title='Task for standard user',
        description='Task description',
        assigned_to=user
    )

    client.login(username='standarduser', password='standardpassword')
    url = reverse('task-detail', kwargs={'pk': task.pk})

    # Standard user trying to update a task they don't have permissions for
    data = {'title': 'Updated Task'}
    response = client.put(url, data, format='json')
    assert response.status_code == 403

    # Admin user should be able to update the task
    client.login(username='admin', password='adminpassword')
    response = client.put(url, data, format='json')
    assert response.status_code == 200
