from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'name', 'parent', 'icon', 'created_at', 'modified_at')
    search_fields = ('name',)
    raw_id_fields = ('parent',)
    ordering = ('index',)


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail', 'logo', 'created_at', 'modified_at')
    search_fields = ('name',)
