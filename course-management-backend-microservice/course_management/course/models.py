from django.db import models

class StudentProgramEnrollment(models.Model):
    student_id = models.IntegerField()
    program_id = models.IntegerField()
    batch_year = models.CharField(max_length=10)
    enrollment_status = models.CharField(max_length=50)
    enrollment_date = models.DateField()
    expected_graduation = models.DateField()
    admission_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SemesterRegistration(models.Model):
    student = models.ForeignKey(StudentProgramEnrollment, on_delete=models.CASCADE)
    semester_id = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    registration_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    total_credits = models.DecimalField(max_digits=5, decimal_places=2)
    registration_date = models.DateField()
    last_date = models.DateField()
    fee_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseRegistration(models.Model):
    student = models.IntegerField()
    course_id = models.IntegerField()
    semester_registration = models.ForeignKey(SemesterRegistration, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    registration_date = models.DateField()
    additional_info = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FacultyCourseAssignment(models.Model):
    faculty_id = models.IntegerField()
    course_id = models.IntegerField()
    semester_id = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    role_type = models.CharField(max_length=50)
    teaching_load = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
