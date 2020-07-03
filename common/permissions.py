from rest_framework.permissions import BasePermission

from . import utils


class ObjectPermission(BasePermission):
    def __init__(self, checker):
        self.checker = checker

    def has_object_permission(self, request, view, object):
        return self.checker(request, view, object)


class IsMember(BasePermission):
    def has_permission(self, request, view):
        return utils.is_member(request.user)


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return utils.is_administrator(request.user)


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return utils.is_manager(request.user)


class IsDefaultUser(BasePermission):
    def has_permission(self, request, view):
        return utils.is_default_user(request.user)
