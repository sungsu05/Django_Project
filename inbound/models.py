from django.db import models
from base.models import Product
from django.utils import timezone


class Inbound(models.Model):
    class MeTa:
        db_table = "inbound"
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    inbound_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.localtime)
    inbound_price = models.PositiveIntegerField()
