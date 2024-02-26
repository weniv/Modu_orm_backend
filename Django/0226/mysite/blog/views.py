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
        # sqlite3에서는 대소문자 구분이 안됩니다. 나중에 배울 postgresql에서는 대소문자 구분이 됩니다.
        # namefield__icontains는 대소문자를 구분하지 않고
        # namefield__contains는 대소문자를 구분합니다.
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
        form = PostForm(request.POST, request.FILES)  # 수정
        if form.is_valid():
            post = form.save()
            # detail로 가야한다!
            # return redirect("blog_details", pk=post.pk)
            return redirect("blog_list")
        else:
            context = {
                "form": form,
                "error": "입력이 잘못되었습니다. 알맞은 형식으로 다시 입력해주세요!",
            }
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
