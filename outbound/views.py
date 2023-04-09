from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import OutBound
from base.models import Product
from inbound.models import Inbound
from inventory.models import Inventory
from inventory.views import inventory
import re

@login_required
def out_bound(request):
    if request.method == "GET":
        return redirect('/')
    elif request.method == 'POST':
        product_code = request.POST.get('product-code')
        outbound_quantity = request.POST.get('outbound_quantity')
        outbound_price = request.POST.get('outbound_price')

        user = request.user
        product = Product.objects.get(code=product_code)


        if str(user) != product.author.username:
            return render(request, 'inbound/inbound.html', {'error':'출고 등록은 상품 등록자만 할 수 있습니다.'})

        #글자 자르고 숫자만 추출
        outbound_price = re.sub(r'[^0-9]', '', outbound_price)
        outbound_quantity = re.sub(r'[^0-9]', '', outbound_quantity)

        # 출고 내역 저장
        new_outbound = OutBound(product=product,outbound_quantity=outbound_quantity,outbound_price=outbound_price)
        new_outbound.save()

        # 출고 합산 내역 저장
        inventory(product_code)
        # 출고 합산 내역 조회
        inventory_ = Inventory.objects.filter(product=product)

        # 총 출고 내역 product__code : product모델의 code 필드 검색
        outbound = OutBound.objects.filter(product__code=product_code).order_by('-outbound_created_at')
        product = Product.objects.filter(code=product_code)

        # 총 입고 내역
        inbound = Inbound.objects.filter(product__code=product_code).order_by('-created_at')

        #
        product_total = Inventory.objects.get(product=product_code)
        profit = product_total.total_outbound_price - product_total.total_inbound_price
        product_total = product_total.total_inbound_quantity - product_total.total_outbound_quantity
        product_info = {
            'profit': profit,
            'product_total': product_total
        }


        # 입고내역과, 상품정보 딕셔너리 리스트에 담기
        context = { 'product':product }
        context.update({ 'outbound':outbound })
        context.update({'inbound':inbound})
        context.update({'inventory':inventory_})
        context.update({'product_info': product_info})

        return render(request, 'inbound/inbound.html', context)
