from django.urls import path
from . import views

urlpatterns = [
    path('out-bound', views.out_bound, name='outbound'),
]
