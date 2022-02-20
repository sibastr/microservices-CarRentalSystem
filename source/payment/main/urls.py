from django.urls import path, include
from .views import PaymentList,PaymentDetail

urlpatterns = [
    path('api/v1/payments', PaymentList.as_view(), name = 'PaymentList'),
    path('api/v1/payments/<uuid:pk>', PaymentDetail.as_view(), name = 'PaymentDetail')
]