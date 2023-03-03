from rest_framework import permissions
from users.models import User


class IsSuperuserOrNo(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
            
        return request.user.is_authenticated and request.user.is_superuser


class IsCritic(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_critic
        return request.method in permissions.SAFE_METHODS

          