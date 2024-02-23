from django.shortcuts import render
from .models import Post
from django.db.models import Q


def blog_list(request):
    if request.GET.get("q"):
        q = request.GET.get("q")
        db = Post.objects.filter(
            Q(title__icontains=q) | Q(contents__icontains=q)
        ).distinct()
    else:
        db = Post.objects.all()
    context = {
        "db": db,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        "db": db,
    }
    return render(request, "blog/blog_detail.html", context)
