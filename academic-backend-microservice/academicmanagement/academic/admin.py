from django.contrib import admin
from .models import Program, Semester, Course, Subject, Lab

admin.site.register(Program)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Lab)
