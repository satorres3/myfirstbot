import pytest
from django.contrib.auth import get_user_model
from hub.models import Department

@pytest.mark.django_db
def test_department_slug_created():
    user = get_user_model().objects.create(username="tester")
    dept = Department.objects.create(name="Research", created_by=user)
    assert dept.slug == "research"
