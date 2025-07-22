from rest_framework import serializers
from .models import ExaminationSchedule, CourseExamination, ExamResult, SemesterResult

class ExaminationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationSchedule
        fields = '__all__'

class CourseExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseExamination
        fields = '__all__'

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'

class SemesterResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterResult
        fields = '__all__'
