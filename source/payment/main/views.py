from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
from .models import Payment
from .serializers import PaymentSerializer
#from cars.pagination import CustomPagination

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



