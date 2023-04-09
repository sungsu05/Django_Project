from inbound.models import Inbound
from outbound.models import OutBound
from base.models import Product
from .models import Inventory
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce

def inventory(code):
    product = Product.objects.get(code=code)
    inventory_item = Inventory.objects.filter(product=product).first()
    if inventory_item:
        # 제품이 있으면 업데이트
        # Coalesce 좌항의 값이 null이라면, 우항의 값을 대입한다.
        inventory_item.total_inbound_price = Coalesce(Inbound.objects.filter(product__code=code).aggregate(Sum('inbound_price')).get('inbound_price__sum'), Value(0))
        inventory_item.total_outbound_price = Coalesce(OutBound.objects.filter(product__code=code).aggregate(Sum('outbound_price')).get('outbound_price__sum'), Value(0))
        inventory_item.total_inbound_quantity = Coalesce(Inbound.objects.filter(product__code=code).aggregate(Sum('inbound_quantity')).get('inbound_quantity__sum'), Value(0))
        inventory_item.total_outbound_quantity = Coalesce(OutBound.objects.filter(product__code=code).aggregate(Sum('outbound_quantity')).get('outbound_quantity__sum'), Value(0))
        inventory_item.save()
    else:

        new_inventory = Inventory(product=product,
                                   total_inbound_price=Coalesce(Inbound.objects.filter(product__code=code).aggregate(Sum('inbound_price')).get('inbound_price__sum'), Value(0)),
                                   total_outbound_price=Coalesce(OutBound.objects.filter(product__code=code).aggregate(Sum('outbound_price')).get('outbound_price__sum'), Value(0)),
                                   total_inbound_quantity=Coalesce(Inbound.objects.filter(product__code=code).aggregate(Sum('inbound_quantity')).get('inbound_quantity__sum'), Value(0)),
                                   total_outbound_quantity=Coalesce(OutBound.objects.filter(product__code=code).aggregate(Sum('outbound_quantity')).get('outbound_quantity__sum'), Value(0))
                                   )
        new_inventory.save()
