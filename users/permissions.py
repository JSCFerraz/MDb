from rest_framework import permissions
from rest_framework.views import View, Request


class IsAllowedUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_superuser:
                return request.user.is_authenticated and request.user.is_superuser
            else:
                return False
        return True
