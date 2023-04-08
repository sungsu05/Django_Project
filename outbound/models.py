from django.db import models
from base.models import Product
# Create your models here.

class OutBound(models.Model):
    class Meta:
        db_table = "out_bound"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    out_bound_quantity = models.PositiveIntegerField()
    out_bound_created_at = models.DateTimeField(auto_now_add=True)
    out_bound_price = models.PositiveIntegerField()

