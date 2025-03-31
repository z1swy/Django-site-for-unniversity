from django.db import models
from users.models import CustomUser

class Institute(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'

class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    institute = models.ForeignKey(Institute, related_name='departments', on_delete=models.CASCADE, verbose_name=u"Институт")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"Название")
    department = models.ForeignKey(Department, related_name='courses', on_delete=models.CASCADE, verbose_name=u"Кафедра")
    year = models.PositiveIntegerField(default=1, verbose_name=u"год")
    teacher = models.ForeignKey(CustomUser, related_name='taught_courses', on_delete=models.CASCADE, verbose_name=u"Преподаватель")
    students = models.ManyToManyField(CustomUser, through='Enrollment', related_name='enrolled_courses', verbose_name=u"Студенты")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Unit(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"Заголовок")
    course = models.ForeignKey(Course, related_name='units', on_delete=models.CASCADE, verbose_name=u"Курс")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

class Lecture(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"Заголовок")
    content = models.TextField(verbose_name=u"Содержание")
    file = models.FileField(upload_to='lectures/', blank=True, null=True, verbose_name=u"Файл")
    unit = models.ForeignKey(Unit, related_name='lectures', on_delete=models.CASCADE, verbose_name=u"Раздел")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'


class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=u"Студент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"Курс")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name=u"Дата регистрации")

    def __str__(self):
        return f'{self.student} enrolled in {self.course}'

    class Meta:
        verbose_name = 'Запись на курсы'
        verbose_name_plural = 'Записи на курсы'
