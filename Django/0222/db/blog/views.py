from django.shortcuts import render
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    context = {"blog_list": blogs}
    return render(request, "blog_list.html", context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {"blog": blog}
    return render(request, "blog_detail.html", context)
