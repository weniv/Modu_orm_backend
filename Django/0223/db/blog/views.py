from django.shortcuts import render, redirect
from .models import Post


def blog_list(request):
    blogs = Post.objects.all()
    context = {"db": blogs}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {"db": blog}
    return render(request, "blog/blog_detail.html", context)


def blog_create(request, title):
    contents = f"hello world {title}"
    q = Post.objects.create(title=title, contents=contents)
    q.save()
    return redirect("blog_list")


def blog_delete(request, pk):
    q = Post.objects.get(pk=pk)
    q.delete()
    return redirect("blog_list")


def blog_test(request):
    return render(request, "blog/blog_test.html")
