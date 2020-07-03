from rest_framework import viewsets
from rest_framework.response import Response

from . import utils
from .permissions import ObjectPermission


class ExtendedModelViewSet(viewsets.ModelViewSet):
    querysets = {}    # default: queryset
    permissions = {}  # default: permission_classes
    serializers = {}  # default: serializer_class

    def get_queryset(self):
        """
        filter by url parameters
        """

        queryset = super().get_queryset()
        fields = []
        if hasattr(self, 'filter_class'):
            fields = self.filter_class.Meta.fields
        elif hasattr(self, 'filter_fields'):
            fields = self.filter_fields
        for field in fields:
            value = self.kwargs.get(field, None)
            if value is not None:
                queryset = queryset.filter(**dict([(field, value)]))
        order_fields = self.get_order_fields()
        if order_fields:
            queryset = queryset.order_by(*order_fields)
        return queryset

    def get_order_fields(self):
        """
        Redefine this method
        """
        return []

    def list(self, request, *args, **kwargs):
        """
        Copy of rest framework code, just for save used queryset.
        But not includes pagination
        """

        queryset = self.filter_queryset(self.get_queryset())
        self.result_queryset = queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        perms = utils.in_dict(self.permissions, self.action) or []
        perms = [perms] if isinstance(perms, type) else perms
        perms = list(perms) + super().get_permissions()
        perms += [ObjectPermission(self.object_permission_check)]
        return [p() if isinstance(p, type) else p for p in perms]

    def object_permission_check(self, request, view, object):
        """
        Redefine this method
        """
        return True

    def get_serializer_class(self):
        return utils.in_dict(self.serializers, self.action, self.serializer_class)
