import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_book_list_status_200(client, django_user_model):
    user = django_user_model.objects.create_user(
        username='testuser', password='testpass123'
    )
    client.force_login(user)
    response = client.get(reverse('book_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_list_requires_login(client):
    response = client.get(reverse('book_list'))
    assert response.status_code == 302