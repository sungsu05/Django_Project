from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Inbound
from base.models import Product

def inbound_create(request):
    return render(request, 'inbound/inbound.html')


# 코드번호로 상품 검색
def search(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        serch_code = request.POST.get('product-code')
        product_code = Product.objects.filter(code=serch_code)
        if product_code:
            return render(request, 'inbound/inbound.html', {'product': product_code})
        else :
            return render(request, 'inbound/inbound.html',{"error":"코드번호와 일치하는 상품이 없습니다."})

def inbound_history(request):
    if request.method == "GET":
        return redirect('/')
    elif request.method == 'POST':
        product_code = request.POST.get('product-code')
        inbound_quantity = request.POST.get('inbound_quantity')
        inbound_price = request.POST.get('inbound_price')
        print(f'코드{product_code} , 가격 {inbound_price} , 수량 {inbound_quantity}')
        return redirect('/')