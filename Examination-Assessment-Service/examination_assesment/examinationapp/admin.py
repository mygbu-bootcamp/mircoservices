from django.contrib import admin
from .models import (
    ExaminationSchedule,
    CourseExamination,
    ExamResult,
    SemesterResult
)

admin.site.register(ExaminationSchedule)
admin.site.register(CourseExamination)
admin.site.register(ExamResult)
admin.site.register(SemesterResult)
