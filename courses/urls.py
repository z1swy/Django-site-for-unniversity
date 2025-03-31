from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'courses/(?P<course_id>\d+)/students', StudentListView, basename='student')
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'units', UnitViewSet)
router.register(r'units/(?P<unit_id>\d+)/lectures', LectureViewSet, basename='unit-lecture')

urlpatterns = [
    path('', include(router.urls)),
]
