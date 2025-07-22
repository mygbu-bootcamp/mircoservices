from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AttendanceSession, AttendanceRecord
from .serializers import AttendanceSessionSerializer, AttendanceRecordSerializer

from attendanceapp.services.academic_client import get_course
from attendanceapp.services.user_client import get_student, get_faculty
from attendanceapp.services.qr_generator import generate_qr_code

class AttendanceSessionCreateView(APIView):
    def post(self, request):
        faculty_id = request.data.get("faculty_id")
        course_id = request.data.get("course_id")

        faculty = get_faculty(faculty_id)
        course = get_course(course_id)

        if not faculty or not course:
            return Response({"error": "Faculty or Course not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AttendanceSessionSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(AttendanceSessionSerializer(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceMarkView(APIView):
    def post(self, request):
        student_id = request.data.get("student_id")
        student = get_student(student_id)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AttendanceRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAttendanceView(APIView):
    def get(self, request, student_id):
        records = AttendanceRecord.objects.filter(student_id=student_id)
        serializer = AttendanceRecordSerializer(records, many=True)
        return Response(serializer.data)

class CourseAttendanceView(APIView):
    def get(self, request, course_id):
        sessions = AttendanceSession.objects.filter(course_id=course_id)
        serializer = AttendanceSessionSerializer(sessions, many=True)
        return Response(serializer.data)

class QRCodeGenerateView(APIView):
    def get(self, request, session_id):
        try:
            session = AttendanceSession.objects.get(pk=session_id)
            qr_data = f"session_id:{session_id}"
            qr_code_base64 = generate_qr_code(qr_data)
            session.qr_code = qr_code_base64
            session.save()
            return Response({"qr_code": qr_code_base64})
        except AttendanceSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
