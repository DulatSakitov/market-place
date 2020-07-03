from rest_framework.serializers import ModelSerializer
from . import models


class ChildrenSerializer(ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'name')


class CategoryListSerializer(ModelSerializer):
    children = ChildrenSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ('id', 'index', 'name', 'parent', 'icon', 'children')


class BrandListSerializer(ModelSerializer):

    class Meta:
        model = models.Brand
        fields = ('id', 'name', 'logo', 'detail')
