from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Проверяет, что пользователь является модератором.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()



