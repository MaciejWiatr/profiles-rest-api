from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profiles."""

    def has_object_permission(self, request, view, obj):
        """Check user is tryng to edit their own profile.

        Args:
            request
            view
            obj
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status

        Args:
            request ([type]): [description]
            view ([type]): [description]
            obj ([type]): [description]
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
