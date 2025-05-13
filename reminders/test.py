from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from .models import Reminder

class ReminderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_reminder(self):
        payload = {
            "message": "Test Reminder",
            "remind_at": timezone.now().isoformat(),
            "method": "email"
        }
        response = self.client.post('/api/reminders/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reminder.objects.count(), 1)

