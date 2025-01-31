from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a profile to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are granted to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the profile
        return obj.owner == request.user
