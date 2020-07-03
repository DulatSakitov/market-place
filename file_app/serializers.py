from rest_framework.serializers import ModelSerializer
from . import models


class FileSerializer(ModelSerializer):

    class Meta:
        model = models.File
        fields = ('id', 'file')
