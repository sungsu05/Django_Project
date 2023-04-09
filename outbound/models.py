from django.db import models
from base.models import Product
# Create your models here.

class OutBound(models.Model):
    class Meta:
        db_table = "out_bound"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    outbound_quantity = models.PositiveIntegerField()
    outbound_created_at = models.DateTimeField(auto_now_add=True)
    outbound_price = models.PositiveIntegerField()

