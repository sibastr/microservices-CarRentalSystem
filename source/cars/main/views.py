from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
from .models import Car
from .serializers import CarSerializer
from cars.pagination import CustomPagination

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer

    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Car.objects.all()

        showAll = self.request.query_params.get('showAll')
        if (showAll == 'false'):
            queryset = queryset.filter(availability = True)
        return queryset


