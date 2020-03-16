from django.db import transaction
from django.dispatch import Signal
from rest_framework import serializers

from . import models, receivers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order

        fields = (
            'id', 'address', 'apartment',
            'price', 'phone', 'status', 'food'
        )
        extra_kwargs = {
            'address': {'write_only': True},
            'apartment': {'write_only': True},
            'phone': {'write_only': True},
            'status': {'write_only': True}
        }

    @transaction.atomic()
    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance