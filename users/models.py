from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"Номер телефона")
    patronymic = models.CharField(max_length=45, blank=True, null=True, verbose_name=u"Отчество")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, verbose_name=u"Группа")
    group_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"Номер группы")

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'