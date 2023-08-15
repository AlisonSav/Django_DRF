from django.urls import include, path
from rest_framework import routers

from hw_20.views import CommentViewSet, PostViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"comment", CommentViewSet, basename="comment")
router.register("post", PostViewSet, basename="post")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
