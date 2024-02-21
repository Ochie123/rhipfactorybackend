from rest_framework import permissions

class IsAuthenticatedOrReadOnlyForDelete(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to delete objects.
    """
    def has_permission(self, request, view):
        # Allow read-only permissions for GET, HEAD, and OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow POST (create) requests for non-authenticated users.
        if request.method == 'POST':
            return True
        # Check if the user is authenticated for all other requests.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow delete permission only if the user is staff or superuser.
        return request.user.is_staff or request.user.is_superuser
