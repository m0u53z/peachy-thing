from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'remind_at', 'method', 'created_at']
    list_filter = ['method', 'remind_at']
    search_fields = ['message']

