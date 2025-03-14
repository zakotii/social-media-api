from rest_framework import serializers
from .models import User, Post, Follower
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["user", "follower", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    hashtags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "content", "media", "created_at", "hashtags"]

    def get_hashtags(self, obj):
        return re.findall(r"#(\w+)", obj.content)
