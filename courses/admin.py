from django.contrib import admin
from .models import *

admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Unit)
admin.site.register(Enrollment)