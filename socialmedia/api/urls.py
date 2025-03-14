from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, FollowerViewSet
from .views import RegisterView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"followers", FollowerViewSet)
from .views import UserCreateView
from .views import RegisterUserView


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", UserCreateView.as_view(), name="user-create"),
    path("register/", RegisterUserView.as_view(), name="register"),
]
