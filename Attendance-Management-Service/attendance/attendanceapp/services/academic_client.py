import requests
from django.conf import settings

def get_course(course_id):
    url = f"{settings.ACADEMIC_SERVICE_URL}/api/courses/{course_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
