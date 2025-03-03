import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_student_list_view(client):
    instance1 = test_helpers.create_student_student()
    instance2 = test_helpers.create_student_student()
    url = reverse("student_student_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_student_create_view(client):
    url = reverse("student_student_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_student_detail_view(client):
    instance = test_helpers.create_student_student()
    url = reverse("student_student_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_student_update_view(client):
    instance = test_helpers.create_student_student()
    url = reverse("student_student_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
