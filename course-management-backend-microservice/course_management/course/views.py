from rest_framework import generics
from .models import StudentProgramEnrollment, SemesterRegistration, CourseRegistration, FacultyCourseAssignment
from .serializers import StudentProgramEnrollmentSerializer, SemesterRegistrationSerializer, CourseRegistrationSerializer, FacultyCourseAssignmentSerializer

class StudentProgramEnrollmentCreateView(generics.CreateAPIView):
    queryset = StudentProgramEnrollment.objects.all()
    serializer_class = StudentProgramEnrollmentSerializer

class SemesterRegistrationCreateView(generics.CreateAPIView):
    queryset = SemesterRegistration.objects.all()
    serializer_class = SemesterRegistrationSerializer

class CourseRegistrationCreateView(generics.CreateAPIView):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer

class FacultyCourseAssignmentCreateView(generics.CreateAPIView):
    queryset = FacultyCourseAssignment.objects.all()
    serializer_class = FacultyCourseAssignmentSerializer

class StudentRegistrationsListView(generics.ListAPIView):
    serializer_class = SemesterRegistrationSerializer

    def get_queryset(self):
        student_id = self.kwargs['id']
        return SemesterRegistration.objects.filter(student__student_id=student_id)
