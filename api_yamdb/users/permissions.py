from rest_framework import permissions


class SelfUserOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.id == request.user)
