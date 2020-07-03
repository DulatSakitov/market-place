from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from . import utils, permissions


class BaseActionHandler(APIView):
    """
    Base action class
    """

    object = None
    model_class = None
    permissions = {}
    permission_classes = []

    # this calls before "get_permissions"
    def initial(self, request, *args, **kwargs):
        self.action = kwargs.get('action', None)
        return super().initial(request, *args, **kwargs)

    def get_permissions(self):
        perms = utils.in_dict(self.permissions, self.action) or []
        perms = [perms] if isinstance(perms, type) else perms
        perms = list(perms) + self.permission_classes
        perms += [permissions.ObjectPermission(self.object_permission_check)]
        return [p() if isinstance(p, type) else p for p in perms]

    def object_permission_check(self, request, view, object):
        """
        Redefine this method
        """
        return True

    def put(self, request, **kwargs):
        return self.handle(**kwargs)

    def handle(self, **kwargs):
        handler = getattr(self, 'action_{}'.format(self.action), None)
        if not handler:
            return utils.error_400_response('bad_action', _('Bad action'))
        kwargs.pop('action', None)
        pk = kwargs.pop('pk', None)
        if pk and self.model_class:
            self.object = get_object_or_404(self.model_class, pk=pk)
            self.check_object_permissions(self.request, self.object)
        result = handler(**kwargs)
        if not isinstance(result, Response):
            if result is not None:
                result = Response(status=202, data=result)
            else:
                result = Response(status=202)
        return result
