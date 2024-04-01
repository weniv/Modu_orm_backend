from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import PostSerializer, CommentSerializer
from .models import Comment, Post, Like
from rest_framework import permissions, views, response, status
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.permission_classes = [permissions.AllowAny]
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["get"])
    def sampleone(self, request, pk=None):
        """
        detail=True: 특정 게시물에 대한 작업
        detail=False: 모든 게시물에 대한 작업
        /posts/{pk}/sampleone/: 개별 게시물의 제목과 내용을 반환하는 엔드포인트 (detail=True)
        """
        data = {"title": "hello", "content": "world"}
        return response.Response(data)

    @action(detail=False, methods=["get"])
    def sampletwo(self, request):
        """
        /posts/sampletwo/: 모든 게시물의 제목과 작성자 이름을 반환하는 엔드포인트 (detail=False)
        """
        data = [{"title": "hello 2", "author": "world 2"}]
        return response.Response(data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs["post_pk"])


class LikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            return response.Response(status=status.HTTP_409_CONFLICT)

        return response.Response(status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(Like, post=post, user=request.user)
        like.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
