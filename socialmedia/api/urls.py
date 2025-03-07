from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import UserViewSet, PostViewSet, FollowerViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"followers", FollowerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
