from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeView

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("posts/(?P<post_pk>[^/.]+)/comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:post_id>/like/", LikeView.as_view(), name="post-like"),
]
