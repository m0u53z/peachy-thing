from django.db import models

class Reminder(models.Model):
    REMINDER_METHODS = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]

    message = models.TextField()
    remind_at = models.DateTimeField()
    method = models.CharField(max_length=10, choices=REMINDER_METHODS)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_method_display()} at {self.remind_at}"

