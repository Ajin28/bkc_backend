# Permissions and Role-based Access
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and request.user.role.name == 'admin'

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and request.user.role.name == 'buyer'

class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        return request.user.role and request.user.role.name == 'supplier'
    
class IsAdminOrSupplier(BasePermission):
    def has_permission(self, request, view):
        # Check if the user's role is either 'admin' or 'supplier'
        return request.user.role and request.user.role.name in ['admin', 'supplier']