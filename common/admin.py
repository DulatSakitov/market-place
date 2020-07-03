from django.contrib import admin
from django.contrib.admin.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
    '__str__', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message')
    list_filter = ('content_type',)
    search_fields = ['user__username', 'change_message', 'object_repr', 'object_id']
    date_hierarchy = 'action_time'


admin.site.register(LogEntry, LogEntryAdmin)
