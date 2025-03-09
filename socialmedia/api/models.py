from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        app_label = "api"

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="api_users",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="api_users_permissions",
        blank=True,
    )


class Follower(models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    follower = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "follower")

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    media = models.ImageField(upload_to="post_media/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at}"
