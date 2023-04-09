from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

#base화면 html 출력
def base(request):
    products = Product.objects.all()
    return render(request, 'base.html',{'products':products})


# 상품 등록
@login_required
def registrations(request):
    if request.method == 'GET':
        return render(request, 'base/product.html')
    #상품 저장
    elif request.method == 'POST':
        product_name = request.POST.get('productName','')
        product_type = request.POST.get('productType','')
        product_size = request.POST.get('productSize','')
        product_price = request.POST.get('productPrice','')
        author = request.user

        new_product = Product(author=author, name=product_name, type=product_type, size=product_size,price=product_price)
        print(new_product.author)


        #상품 코드 번호 부여
        total_products = Product.objects.count()
        code = "{:04d}".format(total_products + 1)
        new_product.code = code
        new_product.save()

        #새로운 html코드를 보여준다.
        products = Product.objects.all()
        return render(request, 'base.html',{'products':products})


# 상품 삭제
@login_required
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.user == product.author:
        product.delete()

    products_code = Product.objects.all().order_by('id')

    # 반복자 i의값을 기준으로 새로운 코드번호가 생성된다.
    for i, p in enumerate(products_code, 1):
        p.code = str(i).zfill(4)
        p.save()

    products = Product.objects.all()
    return render(request, 'base.html', {'products': products})
