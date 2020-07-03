from rest_framework.serializers import ModelSerializer

from dicts.serializers import CategoryListSerializer, BrandListSerializer
from file_app.serializers import FileSerializer
from . import models


class GroupPropertiesSerializer(ModelSerializer):

    class Meta:
        model = models.GroupProperties
        fields = ('id', 'name')


class ProductCharacteristicsSerializer(ModelSerializer):

    class Meta:
        model = models.ProductCharacteristics
        fields = ('id', 'value')


class PropertySerializer(ModelSerializer):
    group = GroupPropertiesSerializer(read_only=True)
    values = ProductCharacteristicsSerializer(many=True)

    class Meta:
        model = models.Property
        fields = ('id', 'name', 'group', 'detail', 'values')


class ProductListSerializer(ModelSerializer):
    characteristics = ProductCharacteristicsSerializer(many=True)
    images = FileSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'category', 'brand', 'images',
                  'characteristics', 'created_at', 'modified_at')


class ProductDetailSerializer(ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    brand = BrandListSerializer(read_only=True)
    images = FileSerializer(many=True)
    characteristics = ProductCharacteristicsSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'category', 'brand', 'images',
                  'characteristics', 'created_at', 'modified_at')
