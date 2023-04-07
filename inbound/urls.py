from django.urls import path
from . import views

urlpatterns = [
    path('inbound/', views.inbound_create, name='inbound'),
    path('product-code-search/', views.search, name='inbound'),

]
