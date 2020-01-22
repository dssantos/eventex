from datetime import datetime

from django.test import TestCase
from django.utils.timezone import now

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
        """Subscribe must have an auto created at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Danilo Santos', str(self.obj))

    def test_subs_today(self):
        self.assertEqual(self.obj.created_at.date(), now().date())

    def test_today_default_to_False(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)