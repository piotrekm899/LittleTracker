import factory
from factory.fuzzy import FuzzyInteger
from api.models import Item, Cart


class ItemFactory(factory.django.DjangoModelFactory):

    external_id = factory.Sequence(lambda n: f"id-abcd-{n}")
    name = factory.Sequence(lambda n: f"name-{n}")
    value = FuzzyInteger(100)

    class Meta:
        model = Item


class CartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Cart
