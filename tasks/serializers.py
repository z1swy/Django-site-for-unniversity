from rest_framework import serializers
from .models import Task, TaskAnswer, TaskAnswerMark
from courses.serializers import UnitSerializer

class TaskReadSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    class Meta:
        model = Task
        fields = '__all__'

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskAnswerReadSerializer(serializers.ModelSerializer):
    task = TaskReadSerializer()

    class Meta:
        model = TaskAnswer
        fields = '__all__'

class TaskAnswerMarkReadSerializer(serializers.ModelSerializer):
    task_answer = TaskAnswerReadSerializer()

    class Meta:
        model = TaskAnswerMark
        fields = '__all__'


class TaskAnswerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAnswer
        fields = '__all__'

class TaskAnswerMarkWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAnswerMark
        fields = '__all__'
