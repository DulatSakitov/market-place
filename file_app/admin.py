from django.contrib import admin
from . import models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'product', 'is_public', 'created_at', 'modified_at')
