from django.db import models
from django.db.models import JSONField

class AttendanceSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    subject_id = models.IntegerField()
    lab_id = models.IntegerField()
    faculty_id = models.IntegerField()
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    session_type = models.CharField(max_length=100)
    topic_covered = models.TextField()
    qr_code = models.TextField(blank=True, null=True)
    location_data = JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AttendanceRecord(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name='records')
    attendance_date = models.DateField()
    marked_at = models.TimeField()
    status = models.CharField(max_length=20)
    location_data = JSONField()
    device_info = models.TextField()
    verification_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AttendanceSummary(models.Model):
    summary_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    course_id = models.IntegerField()
    semester_id = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    total_sessions = models.IntegerField()
    attended_sessions = models.IntegerField()
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

