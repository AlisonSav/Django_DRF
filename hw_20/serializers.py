from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name="post-detail", read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name="comment-detail", read_only=True)

    class Meta:
        model = User
        fields = ("url", "username", "email", "posts", "comments")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("url", "content", "author", "is_published", "category", "created_at")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ("url", "post", "author", "body", "created_at")
