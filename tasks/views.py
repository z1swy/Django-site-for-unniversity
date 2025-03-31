from rest_framework import viewsets
from .models import Task, TaskAnswer, TaskAnswerMark
from .serializers import (
    TaskReadSerializer,
    TaskWriteSerializer,
    TaskAnswerReadSerializer,
    TaskAnswerWriteSerializer,
    TaskAnswerMarkReadSerializer,
    TaskAnswerMarkWriteSerializer
)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskReadSerializer
        return TaskWriteSerializer

class TaskAnswerViewSet(viewsets.ModelViewSet):
    queryset = TaskAnswer.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskAnswerReadSerializer
        return TaskAnswerWriteSerializer

class TaskAnswerMarkViewSet(viewsets.ModelViewSet):
    queryset = TaskAnswerMark.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskAnswerMarkReadSerializer
        return TaskAnswerMarkWriteSerializer
