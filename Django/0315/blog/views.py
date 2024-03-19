from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from rest_framework import serializers
from drf_spectacular.utils import extend_schema

# views.py 수정을 통해 api/schema/swagger-ui 문서를 변경할 수 있도록 수정


# 이 코드는 원래 .serializers.py로 작성이 되었어야 하는 파일입니다.
class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


@extend_schema(
    methods=["GET", "POST"],
    request=PostSerializer,
    responses={200: PostSerializer(many=True)},
)
@api_view(["GET", "POST"])
def blog_list(request):
    serializer = PostSerializer(Post.objects.all(), many=True)
    return Response(serializer.data)
