from django.urls import path, include
from .views import CarList, RentalDetail, RentalList, CarDetail, RentalFinish
urlpatterns = [
    path('api/v1/cars', CarList.as_view(), name='CarList'),
    path('api/v1/cars/<uuid:pk>', CarDetail.as_view(), name='CarDetail'),
    path('api/v1/rental/<uuid:pk>', RentalDetail.as_view(), name='RentalDetail'),
    path('api/v1/rental', RentalList.as_view(), name='RentalList'),
    path('api/v1/rental/<uuid:pk>/finish', RentalFinish.as_view(), name='RentalFinish')
]