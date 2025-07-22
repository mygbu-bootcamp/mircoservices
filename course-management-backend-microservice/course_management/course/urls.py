from django.urls import path
from .views import (
    StudentProgramEnrollmentCreateView,
    SemesterRegistrationCreateView,
    CourseRegistrationCreateView,
    FacultyCourseAssignmentCreateView,
    StudentRegistrationsListView
)

urlpatterns = [
    path('api/enrollments', StudentProgramEnrollmentCreateView.as_view()),
    path('api/semester-registrations', SemesterRegistrationCreateView.as_view()),
    path('api/course-registrations', CourseRegistrationCreateView.as_view()),
    path('api/students/<int:id>/registrations', StudentRegistrationsListView.as_view()),
    path('api/faculty-assignments', FacultyCourseAssignmentCreateView.as_view()),
]
