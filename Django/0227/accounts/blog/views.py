from django.shortcuts import render
from .models import Post


def blog_list(request):
    blogs = Post.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog/blog_list.html", context)


def blog_details(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {"blog": blog}
    return render(request, "blog/blog_detail.html", context)
