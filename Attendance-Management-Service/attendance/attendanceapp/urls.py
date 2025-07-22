from django.urls import path
from .views import (
    AttendanceSessionCreateView,
    AttendanceMarkView,
    StudentAttendanceView,
    CourseAttendanceView,
    QRCodeGenerateView
)

urlpatterns = [
    path(r'sessions', AttendanceSessionCreateView.as_view()),
    path(r'sessions/<int:session_id>/qr', QRCodeGenerateView.as_view()),
    path(r'attendance/mark', AttendanceMarkView.as_view()),
    path(r'attendance/student/<int:student_id>', StudentAttendanceView.as_view()),
    path(r'attendance/course/<int:course_id>', CourseAttendanceView.as_view()),
]

