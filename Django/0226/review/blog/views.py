from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm


def blog_list(request):
    if request.GET.get("q"):
        db = Post.objects.filter(
            Q(title__contains=request.GET.get("q"))
            | Q(contents__contains=request.GET.get("q"))
        ).distinct()
    else:
        db = Post.objects.all()
    context = {"db": db}
    return render(request, "blog/blog_list.html", context)


def blog_details(request, pk):
    db = Post.objects.get(pk=pk)
    context = {"db": db}
    return render(request, "blog/blog_details.html", context)


def blog_create(request):
    if request.method == "GET":
        form = PostForm()
        context = {"form": form}
        return render(request, "blog/blog_create.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # detail로 가야한다!
            # return redirect('blog_details', pk=post.pk)
            return redirect("blog_list")
        else:
            context = {"form": form}
            return render(request, "blog/blog_create.html", context)


def blog_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_details", pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "blog/blog_update.html", context)


def blog_delete(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    print(post)
    if request.method == "POST":
        post.delete()
    return redirect("blog_list")
