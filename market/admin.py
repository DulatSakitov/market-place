from django.contrib import admin
from . import models


@admin.register(models.GroupProperties)
class GroupPropertiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'modified_at')
    search_fields = ('name',)


@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail', 'group', 'is_filter', 'created_at', 'modified_at')
    search_fields = ('name',)
    raw_id_fields = ('group',)
    list_filter = ('is_filter', 'group')


@admin.register(models.ProductCharacteristics)
class ProductCharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'value', 'created_at', 'modified_at')
    search_fields = ('value',)
    raw_id_fields = ('property',)
    list_filter = ('property',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'brand', 'purchase_price',
                    'on_sale', 'is_recommended', 'is_popular', 'is_new',
                    'created_at', 'modified_at')
    ordering = ('id',)
    filter_horizontal = ('characteristics',)
    list_filter = ('category', 'brand', 'on_sale', 'is_recommended', 'is_popular', 'is_new')
    search_fields = ('name',)
