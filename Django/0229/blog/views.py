# 여러가지 테스트
from django.shortcuts import render
from .models import Post
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from django.http import HttpResponse


@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        # print(serializer)
        # print(serializer.data)
        # return Response(100)
        # return Response('hello world')
        # return Response(postlist)  # Queryset을 넘길 때 앞에서 직렬화 하는 코드 있어야 함
        # return Response(serializer.data)
        return HttpResponse(serializer.data)
        # return Response(100)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
