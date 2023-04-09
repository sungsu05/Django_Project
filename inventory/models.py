from django.db import models
from base.models import Product
# Create your models here.

class Inventory(models.Model):
    class Meta:
        db_table='inventory'
    product = models.OneToOneField(Product,on_delete=models.CASCADE)

    #총 입-출고 가격
    total_inbound_price = models.IntegerField()
    total_outbound_price = models.IntegerField()

    #총 입-출고 개수
    total_inbound_quantity = models.IntegerField()
    total_outbound_quantity = models.IntegerField()