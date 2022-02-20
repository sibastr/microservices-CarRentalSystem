from django.urls import path, include
from .views import RentalList, RentalDetail

urlpatterns = [
    path('api/v1/rental', RentalList.as_view(), name = 'RentalList'),
    path('api/v1/rental/<uuid:pk>', RentalDetail.as_view(), name = 'RentalDetail')
]
