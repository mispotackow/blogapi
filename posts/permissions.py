from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешения только на чтение разрешены для любого запроса
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись разрешено только автору сообщения
        return obj.author == request.user