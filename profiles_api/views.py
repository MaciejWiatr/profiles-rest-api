from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile


class HelloApiView(APIView):
    """Test APIView."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        an_apiview = [
            "Uses HTTP methods as function (get,post,patch,put, delete)", "Is similar to a traditional Django View",
            "Gives you the most control over your app logics",
            "Is mapped manually to urls"
        ]

        return Response({'message': "hello!", "an_apiview": an_apiview})

    def post(self, request, format=None):
        """Create hello message with our name."""
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
        """Handle updating an object."""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object."""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello msg."""

        a_viewset = [
            "Uses actions (list,create,retrieve,update,partial_update)",
            "Automatically maps to urls using routers",
            "Proviedes more functionalityt with less codes"
        ]

        return Response({"message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello msg."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            return Response({"message": f"Hello {name}!"})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID."""
        return Response({"httpmethod": "GET"})

    def update(self, request, pk=None):
        """Handle getting an object by its ID."""
        return Response({"httpmethod": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle getting an object by its ID."""
        return Response({"httpmethod": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle getting an object by its ID."""
        return Response({"httpmethod": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens."""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    