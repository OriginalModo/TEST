from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        date_str = self.request.query_params.get('date')
        if date_str:
            date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
            return self.queryset.filter(start_time__date=date)
        return self.queryset


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def testik(request):
    return render(request, template_name='orders/hee.html')