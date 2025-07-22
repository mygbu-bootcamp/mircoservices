import requests
from django.conf import settings

def get_student(student_id):
    url = f"{settings.USER_SERVICE_URL}/api/students/{student_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def get_faculty(faculty_id):
    url = f"{settings.USER_SERVICE_URL}/api/faculty/{faculty_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
