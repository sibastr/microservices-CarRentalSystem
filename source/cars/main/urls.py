from django.urls import path, include
from .views import CarList,CarDetail

urlpatterns = [
    path('api/v1/cars', CarList.as_view(), name = 'CarList'),
    path('api/v1/cars/<uuid:pk>', CarDetail.as_view(), name = 'CarDetail')
]