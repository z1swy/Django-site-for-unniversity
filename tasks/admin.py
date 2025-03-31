from django.contrib import admin

from .models import Task, TaskAnswer, TaskAnswerMark


admin.site.register(Task)
admin.site.register(TaskAnswer)
admin.site.register(TaskAnswerMark)

admin.site.site_title = 'КНИТУ'
admin.site.site_header = 'Администрирование КНИТУ'