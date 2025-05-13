from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer
from .models import Reminder

class ReminderCreateView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List all reminders.
        """
        qs = Reminder.objects.all().order_by('-remind_at')
        serializer = ReminderSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Create a new reminder.
        """
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            reminder = serializer.save()
            return Response({
                'message': 'Reminder saved successfully',
                'reminder': ReminderSerializer(reminder).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

