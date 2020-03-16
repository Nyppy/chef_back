from django.db import models


class Order(models.Model):
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=128)
    price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    phone = models.CharField(max_length=32)
    food = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "order"

    def __str__(self):
        return str(self.pk)


