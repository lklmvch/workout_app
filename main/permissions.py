from rest_framework import permissions

class IsTrainer(permissions.BasePermission):
    """
    Custom permission to allow only users in the 'Trainers' group.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Trainers').exists()

class IsRegularUser(permissions.BasePermission):
    """
    Custom permission to allow only users in the 'Regular Users' group.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Regular Users').exists()
