# exams/urls.py

from rest_framework.routers import DefaultRouter
from .views import ExaminationScheduleViewSet, ExamResultViewSet, SemesterResultViewSet, CourseExaminationViewSet

router = DefaultRouter()
router.register(r'exam-schedules', ExaminationScheduleViewSet)
router.register(r'results', ExamResultViewSet)
router.register(r'semester-results', SemesterResultViewSet)
router.register(r'course-examinations', CourseExaminationViewSet)

urlpatterns = router.urls
