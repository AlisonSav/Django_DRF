from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):  # noqa DJ10, DJ11
    content = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Post: {self.content}, by {self.author}"


class Comment(models.Model):  # noqa DJ10, DJ11
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.body
