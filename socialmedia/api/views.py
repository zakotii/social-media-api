from rest_framework import viewsets, permissions
from .models import User, Post, Follower
from .serializers import UserSerializer, PostSerializer, FollowerSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


from rest_framework.permissions import AllowAny


from rest_framework import generics
from django.contrib.auth import get_user_model

from django.db.models import Q

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    ermission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(
            Q(author=user) | Q(author__followers__follower=user)
        ).distinct()

        hashtag = self.request.query_params.get("hashtag")
        if hashtag:
            queryset = queryset.filter(content__icontains=f"#{hashtag}")

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]
