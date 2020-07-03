from django.shortcuts import render
from rest_framework.permissions import AllowAny

from common.viewsets import ExtendedModelViewSet
from . import models, serializers, filters


class PropertyModelView(ExtendedModelViewSet):
    """
    Получение динамических фильтров.
    &search={text} - полнотекстовый поиск по фильтрам
    &category={id} - получение списка фильтров определенной категории
    """

    queryset = models.Property.objects.filter(is_filter=True)
    permission_classes = (AllowAny,)
    serializers = {'list': serializers.PropertySerializer}
    pagination_class = None
    search_fields = ('name',)
    filter_class = filters.PropertyFilter


class ProductModelView(ExtendedModelViewSet):
    # """
    #     Получение списка товаров или объект товара
    #     Доступны следующие фильтры:
    #     &search={text} - полнотекстовый поиск по товарам (наименование товара, бренда, категории, характеристикам)
    #     &category={id} - по категории с возможностью множественного выбора (при дублировании фильтра применяется оба)
    #     &brand={id} - по бренду с возможностью множественного выбора (при дублировании фильтра применяется оба)
    #     &characteristics={id} - по динамическим характеристикам с возможностью множественного выбора (при дублировании фильтра применяется оба)
    #     &recommended=True - получить список рекоммендованных товаров
    #     &popular=True - получить список популярных товаров
    #     &new=True - получить список новинок
    #     &max_price={price} - ограничение по максимальной цене
    #     &min_price={price} - ограничение по минимальной цене
    #     &by_price_cheap=True - сортировка по убывающей цене
    #     &by_price_exp - сортировка по возрастающей цене
    # """

    queryset = models.Product.objects.filter(on_sale=True)
    permission_classes = (AllowAny,)
    serializers = {
        'retrieve': serializers.ProductDetailSerializer,
        'list': serializers.ProductListSerializer}
    filter_class = filters.ProductFilter
    search_fields = ('name', 'category__name', 'brand__name',
                     'characteristics__value')
