from django.urls import path, re_path
from django.views.generic import DetailView

from .views import OrderList, OrderCreate, testik

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/create/', OrderCreate.as_view(), name='order-create'),
    re_path(r'\w+/', testik),
]