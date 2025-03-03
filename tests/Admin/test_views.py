import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Admin_list_view(client):
    instance1 = test_helpers.create_Admin_Admin()
    instance2 = test_helpers.create_Admin_Admin()
    url = reverse("Admin_Admin_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Admin_create_view(client):
    url = reverse("Admin_Admin_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Admin_detail_view(client):
    instance = test_helpers.create_Admin_Admin()
    url = reverse("Admin_Admin_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Admin_update_view(client):
    instance = test_helpers.create_Admin_Admin()
    url = reverse("Admin_Admin_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
