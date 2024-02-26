from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        request.user.groups.filter(name='Moderator').exists()


class IsProprietor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.proprietor
