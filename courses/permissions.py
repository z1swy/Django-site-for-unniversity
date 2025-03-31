from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.unit.course.teacher == request.user
