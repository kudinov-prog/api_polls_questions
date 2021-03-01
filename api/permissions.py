from rest_framework import permissions


class PollPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class QuestionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
