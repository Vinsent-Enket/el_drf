from rest_framework.permissions import BasePermission


class IsTrueUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user.groups.filter(name='Moderator').exists()


class IsLmsCreator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='LMS_Creator').exists()


class IsProprietor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.proprietor
