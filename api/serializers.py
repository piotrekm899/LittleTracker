from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    external_id = serializers.CharField(max_length=1000)
    name = serializers.CharField(required=False, allow_blank=True)
    value = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = ("external_id", "name", "value")
