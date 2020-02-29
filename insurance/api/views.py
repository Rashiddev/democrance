from rest_framework import generics
from rest_framework.permissions import AllowAny

from insurance.api.serializers import CustomerCreateSerializer, CustomerListSerializer, PolicyCreateSerializer
from insurance.models import Customer, Policy


class CustomerCreateAPIView(generics.CreateAPIView):
    """
    API view to create a new customer.

    Parameters

    :param first_name: First name of the customer.

    :param last_name: Last name of the customer.

    :param dob: Date of birth of the customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    permission_classes = (AllowAny,)


class CustomerListAPIView(generics.ListAPIView):
    """ API view to list all customers. """

    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer
    permission_classes = (AllowAny,)


class PolicyCreateAPIView(generics.CreateAPIView):
    """
    API view to create a new policy.

    Parameters

    :param type: Type of the policy. Available value is "personal-accident".

    :param premium: Premium value of the customer.

    :param cover: Cover value of the customer.

    :param customer: Id of of the customer.
    """

    queryset = Policy.objects.all()
    serializer_class = PolicyCreateSerializer
    permission_classes = (AllowAny,)
