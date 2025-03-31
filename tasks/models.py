from django.db import models

from users.models import CustomUser
import courses.models
from courses.models import Unit


class Task(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=u"Модуль")
    name = models.CharField(max_length=100, verbose_name=u"Задание")
    text = models.TextField(verbose_name=u"Текст")
    files = models.FileField(blank=True, null=True, verbose_name=u"Файлы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class TaskAnswer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name=u"Задание")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    text = models.TextField(verbose_name=u"Текст ответа")
    files = models.FileField(blank=True, null=True, verbose_name=u"Файлы ответа")

    def __str__(self):
        return str(self.pk)


    class Meta:
        verbose_name = 'Ответ на задание'
        verbose_name_plural = 'Ответы на задания'


class TaskAnswerMark(models.Model):
    task_answer = models.OneToOneField(TaskAnswer, on_delete=models.CASCADE, verbose_name=u"Ответ на задание")
    mark = models.IntegerField(verbose_name=u"Оценка")

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Оценка на задание'
        verbose_name_plural = 'Оценки на задания'
