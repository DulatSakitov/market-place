from django.shortcuts import render
from rest_framework.permissions import AllowAny

from common.viewsets import ExtendedModelViewSet
from . import models, serializers, filters


class CategoryModelView(ExtendedModelViewSet):
    """
    Получение списка категорий.
    Доступны следующие фильтры:
    &parent={id} - получение списка дочерних категорий к заданной категории по id
    &search={text} - полнотекстовый поиск по категориям
    &main=True - получение списка главных категорий
    &finite=True - получение списка конечных категорий (не имеющих дочерние)
    &brand={id} - получение списка категорий определенного бренда
    """

    queryset = models.Category.objects.all().order_by('index')
    permission_classes = (AllowAny,)
    serializers = {'list': serializers.CategoryListSerializer}
    pagination_class = None
    search_fields = ('name',)
    filter_class = filters.CategoryFilter


class BrandModelView(ExtendedModelViewSet):
    """
    list:
    Получение списка брендов.
    Доступны следующие фильтры
    &search={text} - полнотекстовый поиск по брендам
    &category={id} - получение списка брендов определенной категории
    """

    queryset = models.Brand.objects.all()
    permission_classes = (AllowAny,)
    serializers = {'list': serializers.BrandListSerializer}
    pagination_class = None
    search_fields = ('name',)
    filter_class = filters.BrandFilter

