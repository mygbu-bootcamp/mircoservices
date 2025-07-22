# exams/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import ExaminationSchedule, CourseExamination, ExamResult, SemesterResult
from .serializers import (
    ExaminationScheduleSerializer,
    CourseExaminationSerializer,
    ExamResultSerializer,
    SemesterResultSerializer
)

class ExaminationScheduleViewSet(viewsets.ModelViewSet):
    queryset = ExaminationSchedule.objects.all()
    serializer_class = ExaminationScheduleSerializer

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        schedule = self.get_object()
        courses = schedule.courses.all()
        serializer = CourseExaminationSerializer(courses, many=True)
        return Response(serializer.data)

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

    @action(detail=False, methods=['get'], url_path='student/(?P<student_id>[^/.]+)')
    def student_results(self, request, student_id=None):
        results = ExamResult.objects.filter(student_id=student_id)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='semester/(?P<semester_id>[^/.]+)')
    def semester_results(self, request, semester_id=None):
        semester_results = SemesterResult.objects.filter(semester_id=semester_id)
        serializer = SemesterResultSerializer(semester_results, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def analytics(self, request):
        total_students = ExamResult.objects.values('student_id').distinct().count()
        pass_count = ExamResult.objects.filter(grade__in=['A', 'B', 'C']).values('student_id').distinct().count()
        pass_percentage = (pass_count / total_students) * 100 if total_students else 0

        grade_distribution = ExamResult.objects.values('grade').annotate(count=Count('grade'))
        distribution = {item['grade']: item['count'] for item in grade_distribution}

        return Response({
            "total_students": total_students,
            "pass_percentage": pass_percentage,
            "grade_distribution": distribution
        })

class SemesterResultViewSet(viewsets.ModelViewSet):
    queryset = SemesterResult.objects.all()
    serializer_class = SemesterResultSerializer

class CourseExaminationViewSet(viewsets.ModelViewSet):
    queryset = CourseExamination.objects.all()
    serializer_class = CourseExaminationSerializer
