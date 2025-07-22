from rest_framework import serializers
from .models import StudentProgramEnrollment, SemesterRegistration, CourseRegistration, FacultyCourseAssignment

class StudentProgramEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgramEnrollment
        fields = '__all__'

class SemesterRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterRegistration
        fields = '__all__'

class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = '__all__'

class FacultyCourseAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyCourseAssignment
        fields = '__all__'
