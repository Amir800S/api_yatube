from rest_framework import permissions


class IsOwnerOfObject(permissions.BasePermission):
    """Проверка доступа к удалению и редактированию."""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
