from django.db import models
import uuid


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Item(models.Model):
    external_id = models.CharField(max_length=1000, unique=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    cart = models.ForeignKey(
        Cart,
        blank=True,
        null=True,
        on_delete=models.SET(None),
        related_name='items'
    )
