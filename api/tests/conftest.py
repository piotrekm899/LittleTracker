import pytest
from rest_framework.test import APIClient

from .factories import ItemFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def item():
    return ItemFactory()


@pytest.fixture
def other_item():
    return ItemFactory()
