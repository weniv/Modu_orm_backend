from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        content = {
            "posts": [{"title": post.title, "content": post.content} for post in posts]
        }
        return Response(content)
    elif request.method == "POST":
        print(request.data)
        title = request.data["title"]
        content = request.data["content"]
        post = Post.objects.create(title=title, content=content)
        post.save()
        return Response({"message": "글 작성 완료!"})
