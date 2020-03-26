from pytest import mark
from rest_framework.reverse import reverse
from rest_framework import status

pytest_plugins = ["docker_compose"]


def _add_item_to_cart(api_client, data):
    url = reverse("add-item-to-cart")
    return api_client.post(url, data)


def _extract_id_as_data(item):
    return {"external_id": item.external_id}


NEW_NAME = "NEW_NAME"
NEW_VALUE = 100


def _prepare_new_data(item):
    return {"external_id": item.external_id,
            "name": NEW_NAME,
            "value": NEW_VALUE
            }


@mark.django_db
def test_add_item_to_cart(api_client, item):
    item_data = _extract_id_as_data(item)
    response = _add_item_to_cart(api_client, item_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@mark.django_db
def test_add_two_items_to_cart(api_client, item, other_item):
    item_data = _extract_id_as_data(item)
    _add_item_to_cart(api_client, item_data)
    other_item_data = _extract_id_as_data(other_item)
    _add_item_to_cart(api_client, other_item_data)
    item.refresh_from_db()
    other_item.refresh_from_db()
    assert item.cart == other_item.cart


@mark.django_db
def test_add_item_without_id(api_client):
    response = _add_item_to_cart(api_client, {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@mark.django_db
def test_add_the_same_item_twice(api_client, item):
    item_data = _extract_id_as_data(item)
    _add_item_to_cart(api_client, item_data)

    new_item_data = _prepare_new_data(item)
    _add_item_to_cart(api_client, new_item_data)

    item.refresh_from_db()
    assert item.name == NEW_NAME
    assert item.value == NEW_VALUE
