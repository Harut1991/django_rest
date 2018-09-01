from rest_framework import permissions

SAFE_METHODS = [ 'POST', 'DELETE']

class IsAuthenticatedAndAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS and request.user.is_staff:
            return False
        return True