from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get,post,patch,put, delete)", "Is similar to a traditional Django View",
            "Gives you the most control over your app logics",
            "Is mapped manually to urls"
        ]

        return Response({'message': "hello!", "an_apiview": an_apiview})
