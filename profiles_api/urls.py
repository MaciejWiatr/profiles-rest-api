from django.urls import path, include
from .views import HelloApiView, HelloViewSet,UserProfileViewSet
from rest_framework.routers import DefaultRouter

app_name = "profiles_api"

ROUTER = DefaultRouter()
ROUTER.register("hello-viewset", HelloViewSet, basename="hello-viewset")
ROUTER.register("profile", UserProfileViewSet)

urlpatterns = [
    path("hello-view/", HelloApiView.as_view()),
    path("", include(ROUTER.urls))
]
