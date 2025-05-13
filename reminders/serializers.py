from rest_framework import serializers
from .models import Reminder
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    # accept date and time separately
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)

    class Meta:
        model = Reminder
        # write_only: date/time; read_only: remind_at is returned
        fields = ['id', 'message', 'method', 'date', 'time', 'remind_at']
        read_only_fields = ['id', 'remind_at']

    def create(self, validated_data):
        # pop date & time, combine into a datetime
        date = validated_data.pop('date')
        time = validated_data.pop('time')
        remind_dt = datetime.combine(date, time)
        # if using USE_TZ=True, you may want:
        # from django.utils import timezone
        # remind_dt = timezone.make_aware(remind_dt)
        validated_data['remind_at'] = remind_dt
        return super().create(validated_data)

