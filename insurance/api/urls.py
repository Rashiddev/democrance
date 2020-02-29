from django.urls import path

from insurance.api.views import CustomerCreateAPIView, CustomerListAPIView, PolicyCreateAPIView

urlpatterns = [
    path('v1/create_customer/', CustomerCreateAPIView.as_view(), name='customer-create'),
    path('v1/create_policy/', PolicyCreateAPIView.as_view(), name='policy-create'),
    path('v1/customers/', CustomerListAPIView.as_view(), name='customer-list')
]