from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from base.models import Product
from .models import Inbound
from outbound.models import OutBound
from inventory.models import Inventory
from inventory.views import inventory
import re

def inbound_create(request):
    return render(request, 'inbound/inbound.html')


# 코드번호로 상품 검색
def search(request):
    context = {}
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        #상품 조회
        search_code = request.POST.get('product-code')
        search_code = str(search_code).zfill(4)

        product = Product.objects.filter(code=search_code)

        if not product:
            context['error'] = '코드번호와 일치하는 상품이 없습니다.'
        else :
            #상품의 입고내역 조회
            search_product = Product.objects.get(code=search_code)
            inbound = Inbound.objects.filter(product=search_product).order_by('-created_at')

            #상품의 출고내역 조회
            outbound = OutBound.objects.filter(product=search_product).order_by(('-outbound_created_at'))

            #상품의 입출고 합산 내역 조회
            inventory = Inventory.objects.filter(product=search_product)

            # 상품의 총 재고량 , 영업 이익
            product_total = Inventory.objects.get(product=search_product)
            profit = product_total.total_outbound_price - product_total.total_inbound_price
            product_total = product_total.total_inbound_quantity - product_total.total_outbound_quantity
            product_info ={
                'profit' : profit,
                'product_total' : product_total
            }

            #context에 두 딕셔너리 추가
            context = {'product': product}
            context.update({'inbound':inbound})
            context.update({'outbound':outbound})
            context.update({'inventory':inventory})
            context.update({'product_info':product_info})



        return render(request, 'inbound/inbound.html', context)

@login_required
def inbound_history(request):
    if request.method == "GET":
        return redirect('/')
    elif request.method == 'POST':
        product_code = request.POST.get('product-code')
        inbound_quantity = request.POST.get('inbound_quantity')
        inbound_price = request.POST.get('inbound_price')

        user = request.user
        product = Product.objects.get(code=product_code)


        if str(user) != product.author.username:
            return render(request, 'inbound/inbound.html', {'error':'입고 등록은 상품 등록자만 할 수 있습니다.'})

        #글자 자르고 숫자만 추출
        inbound_price = re.sub(r'[^0-9]', '', inbound_price)
        inbound_quantity = re.sub(r'[^0-9]', '', inbound_quantity)

        # 입고 내역 저장
        new_inbound = Inbound(product=product,inbound_quantity=inbound_quantity,inbound_price=inbound_price)
        new_inbound.save()

        # 입고 합산 내역 저장
        inventory(product_code)
        # 입고 합산 내역 조회
        inventory_ = Inventory.objects.filter(product=product)

        # 총 입고 내역 product__code : product모델의 code 필드 검색
        inbound = Inbound.objects.filter(product__code=product_code).order_by('-created_at')
        product = Product.objects.filter(code=product_code)

        product_total = Inventory.objects.get(product=product_code)
        profit = product_total.total_outbound_price - product_total.total_inbound_price
        product_total = product_total.total_inbound_quantity - product_total.total_outbound_quantity
        product_info = {
            'profit': profit,
            'product_total': product_total
        }


        # 입고내역과, 상품정보 딕셔너리 리스트에 담기
        context = { 'product':product }
        context.update({ 'inbound':inbound })
        context.update({'inventory': inventory_})
        context.update({'product_info': product_info})

        return render(request, 'inbound/inbound.html', context)