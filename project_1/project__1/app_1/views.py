from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import NumberSerializer

class Classify_Api(APIView):
    serializer_class = NumberSerializer
    def post(self, request):
        """Handles POST requests by accepting a number from request body (JSON)."""
        serializer = NumberSerializer(data=request.data)  # Use request.data for POST

        if serializer.is_valid():
            number_data = serializer.get_number_properties(serializer.validated_data['number'])
            return Response(number_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
