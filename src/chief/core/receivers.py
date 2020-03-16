from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models, services


@receiver(post_save, sender=models.Order)
def order_callback(sender, instance, **kwargs):
    if not instance.status:
        instance.status = True
        instance.save()
        services.SmsManager().send(
            instance.address, instance.apartment, instance.price, instance.phone, instance.food, instance.pk
        )