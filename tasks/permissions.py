from rest_framework import permissions


from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_superuser


class IsStandardUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_superuser


class IsAssignedUserOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.is_staff and request.user.is_superuser:
            return True
        # Standard user can only perform actions on tasks assigned to them
        return obj.assigned_to == request.user
