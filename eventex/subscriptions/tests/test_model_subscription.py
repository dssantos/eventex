from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Danilo Santos',
            cpf='12345678901',
            email='danilo@oi.com',
            phone='71-999999999'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscribe must have an auto created at atribut"""
        self.assertIsInstance(self.obj.created_at, datetime)