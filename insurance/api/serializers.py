from rest_framework import serializers

from insurance.models import Customer, Policy


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'dob')


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob')


class PolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('type', 'premium', 'cover', 'customer')

    def __init__(self, *args, **kwargs):
        super(PolicyCreateSerializer, self).__init__(*args, **kwargs)
        self.fields['customer'].required = True
