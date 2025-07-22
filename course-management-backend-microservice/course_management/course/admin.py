from django.contrib import admin
from .models import (
    StudentProgramEnrollment,
    SemesterRegistration,
    CourseRegistration,
    FacultyCourseAssignment
)

@admin.register(StudentProgramEnrollment)
class StudentProgramEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'program_id', 'batch_year', 'enrollment_status', 'enrollment_date', 'expected_graduation')
    search_fields = ('student_id', 'program_id', 'batch_year', 'enrollment_status')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SemesterRegistration)
class SemesterRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'semester_id', 'academic_year', 'registration_type', 'status', 'total_credits', 'registration_date')
    search_fields = ('academic_year', 'registration_type', 'status')
    list_filter = ('registration_type', 'status')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course_id', 'semester_registration', 'registration_type', 'status', 'registration_date')
    search_fields = ('student', 'course_id', 'status')
    list_filter = ('status', 'registration_type')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FacultyCourseAssignment)
class FacultyCourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculty_id', 'course_id', 'semester_id', 'academic_year', 'role_type')
    search_fields = ('faculty_id', 'course_id', 'academic_year', 'role_type')
    list_filter = ('role_type',)
    readonly_fields = ('created_at', 'updated_at')
