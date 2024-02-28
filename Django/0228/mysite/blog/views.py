from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm


def blog_list(request):
    posts = Post.objects.all()
    return render(request, "blog/blog_list.html", {"posts": posts})


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, "blog/blog_detail.html", {"post": post, "form": form})


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "blog/blog_list.html", {"posts": posts})
