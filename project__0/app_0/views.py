

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import os

class InfoView(APIView):
    def get(self, request):
        return Response({
            "email": os.environ.get('EMAIL', 'ojugbelelateef2006@gmail.com'),
            "current_datetime": datetime.utcnow().isoformat() + "Z",
            "github_url": "https://github.com/abdullateef2006/hng-django-api"
        })