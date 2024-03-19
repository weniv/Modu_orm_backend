from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentCreateView,
    CommentListView,
    LikeView,
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post-list"),  # 게시물 리스트
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # 게시물 상세보기
    path("create/", PostCreateView.as_view(), name="post-create"),  # 게시물 생성
    path("comments/", CommentCreateView.as_view(), name="comment-create"),  # 댓글 생성
    path(
        "<int:post_id>/comments/", CommentListView.as_view(), name="comment-list"
    ),  # 댓글 리스트
    path(
        "<int:post_id>/like/", LikeView.as_view(), name="post-like"
    ),  # 게시물에 대한 좋아요
]
