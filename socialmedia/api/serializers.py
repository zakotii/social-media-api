from rest_framework import serializers
from .models import User, Post, Follower


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


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
