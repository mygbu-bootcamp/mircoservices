from django.contrib import admin
from .models import AttendanceSession, AttendanceRecord, AttendanceSummary

@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = (
        'session_id', 'course_id', 'subject_id', 'lab_id', 'faculty_id',
        'session_date', 'start_time', 'end_time', 'session_type', 'is_active'
    )
    search_fields = ('topic_covered', 'session_type')
    list_filter = ('session_date', 'course_id', 'faculty_id', 'is_active')
    readonly_fields = ('created_at', 'updated_at', 'qr_code')
    ordering = ('-session_date',)

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = (
        'attendance_id', 'student_id', 'session', 'attendance_date',
        'marked_at', 'status', 'verification_method'
    )
    search_fields = ('student_id', 'device_info')
    list_filter = ('attendance_date', 'status')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-attendance_date',)

@admin.register(AttendanceSummary)
class AttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = (
        'summary_id', 'student_id', 'course_id', 'semester_id',
        'academic_year', 'total_sessions', 'attended_sessions', 'attendance_percentage'
    )
    search_fields = ('student_id', 'academic_year')
    list_filter = ('academic_year', 'course_id', 'semester_id')
    readonly_fields = ('created_at', 'updated_at', 'last_updated')
    ordering = ('-last_updated',)
