from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get,post,patch,put, delete)", "Is similar to a traditional Django View",
            "Gives you the most control over your app logics",
            "Is mapped manually to urls"
        ]

        return Response({'message': "hello!", "an_apiview": an_apiview})

    def post(self, request, format=None):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            msg = f"Hello {name}!"
            return Response({"message": msg})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})
