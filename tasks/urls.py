from django.urls import include, path
from rest_framework import routers
from .views import TaskViewSet, TaskAnswerViewSet, TaskAnswerMarkViewSet


router = routers.DefaultRouter()
router.register(r'units/(?P<unit_id>\d+)/tasks', TaskViewSet, basename='unit-task')
router.register(r'units/(?P<unit_id>\d+)/answers', TaskAnswerViewSet, basename='unit-answer')
router.register(r'units/(?P<unit_id>\d+)/marks', TaskAnswerMarkViewSet, basename='unit-mark')

urlpatterns = [
    path('', include(router.urls)),
]