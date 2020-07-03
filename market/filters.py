from decimal import Decimal

from django_filters import CharFilter

from common.filters import FilterSet
from . import models
from market import models as market_models


class PropertyFilter(FilterSet):
    category = CharFilter(method='filter_category')

    class Meta:
        model = models.Property
        fields = []

    def filter_category(self, queryset, name, value):
        categories = market_models.Product.objects.filter(category_id=value, is_public=True).values_list('category')
        return queryset.filter(id__in=categories)


class ProductFilter(FilterSet):
    category = CharFilter(method='filter_category')
    brand = CharFilter(method='filter_brand')
    characteristics = CharFilter(method='filter_characteristics')
    recommended = CharFilter(method='filter_recommended')
    popular = CharFilter(method='filter_popular')
    new = CharFilter(method='filter_new')
    max_price = CharFilter(method='filter_max_price')
    min_price = CharFilter(method='filter_min_price')
    by_price_cheap = CharFilter(method='filter_by_price_cheap')
    by_price_exp = CharFilter(method='filter_by_price_exp')

    def filter_category(self, queryset, name, value):
        return queryset.filter(category__in=self.request.GET.getlist('category'))

    def filter_brand(self, queryset, name, value):
        return queryset.filter(brand__in=self.request.GET.getlist('brand'))

    def filter_characteristics(self, queryset, name, value):
        result = queryset
        for c in self.request.GET.getlist('characteristics'):
            result = result.filter(characteristics__in=[c])
        return result

    def filter_recommended(self, queryset, name, value):
        return queryset.filter(is_recommended=True)

    def filter_popular(self, queryset, name, value):
        return queryset.filter(is_popular=True)

    def filter_new(self, queryset, name, value):
        return queryset.filter(is_new=True)

    def filter_min_price(self, queryset, name, value):
        return queryset.filter(price__gt=Decimal(value))

    def filter_max_price(self, queryset, name, value):
        return queryset.filter(price__lt=Decimal(value))

    def filter_by_price_exp(self, queryset, value):
        return queryset.order_by('-total_price')

    def filter_by_price_cheap(self, queryset, value):
        return queryset.order_by('total_price')

    class Meta:
        model = models.Product
        fields = []
