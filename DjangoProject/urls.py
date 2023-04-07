from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 페이지
    path('',include('user.urls')), # user app url 연결
    path('',include('base.urls')), # base app url 연결
    path('',include('inbound.urls')), # inbound app url 연결
]
