from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
from .models import Rental
from .serializers import RentalSerializer


class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        queryset = Rental.objects.all()
        username = self.request.headers.get('X-User-Name', None)

        if (username):
            queryset = queryset.filter(username=username)
        return queryset




