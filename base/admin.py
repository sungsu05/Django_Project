from django.contrib import admin
# django에서 admin툴을 사용하겠다는 의미
from .models import Product
# 우리가 생성한 모델을 가져오는 것

admin.site.register(Product)
