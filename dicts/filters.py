from django_filters import CharFilter

from common.filters import FilterSet
from . import models
from market import models as market_models


class CategoryFilter(FilterSet):
    main = CharFilter(method='filter_main')
    finite = CharFilter(method='filter_finite')
    brand = CharFilter(method='filter_brand')

    class Meta:
        model = models.Category
        fields = ['parent']

    def filter_main(self, queryset, name, value):
        return queryset.filter(parent=None)

    def filter_finite(self, queryset, name, value):
        return queryset.filter(children=[])

    def filter_brand(self, queryset, name, value):
        categories = market_models.Product.objects.filter(brand_id=value, on_sale=True).values_list('category')
        return queryset.filter(id__in=categories)


class BrandFilter(FilterSet):
    category = CharFilter(method='filter_category')

    class Meta:
        model = models.Brand
        fields = []

    def filter_category(self, queryset, name, value):
        brands = market_models.Product.objects.filter(category_id=value, on_sale=True).values_list('brand')
        return queryset.filter(id__in=brands)
