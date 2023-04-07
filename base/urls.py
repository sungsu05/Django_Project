from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('product/', views.registrations, name='product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

]
