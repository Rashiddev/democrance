import json

from django.test import TestCase, Client

# initialize the APIClient app
from django.urls import reverse
from rest_framework import status

from insurance.models import Customer

client = Client()

class CreateNewCustomerTest(TestCase):
    """ Test module for inserting a new customer """
    def setUp(self):
        self.valid_payload = {
            'first_name': 'Rashid',
            'last_name': 'Mahmood',
            'dob': '1991-11-04'
        }
        self.invalid_payload = {
            'first_name': 'Ali',
            'last_name': 'Hassan',
            'dob': '04-11-11'
        }

    def test_create_valid_customer(self):
        response = client.post(
            path=reverse('insurance-api:customer-create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        response = client.post(
            path=reverse('insurance-api:customer-create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateNewPolicyTest(TestCase):
    """ Test module for inserting a new policy """
    def setUp(self):
        customer = Customer.objects.create(
            first_name='Rashid',
            last_name='Mahmood',
            dob='1991-11-04'
        )

        self.valid_payload = {
            "type": "personal-accident",
            "premium": 200,
            "cover": 200000,
            "customer": customer.id
        }
        self.invalid_payload = {
            "type": "abc-test",
            "premium": 200,
            "cover": 200000,
            "customer": customer.id
        }

    def test_create_valid_customer(self):
        response = client.post(
            path=reverse('insurance-api:policy-create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        response = client.post(
            path=reverse('insurance-api:policy-create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

