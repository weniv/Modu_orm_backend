from django.shortcuts import render, redirect
from .models import Post, Comment, Tag, Subscription  # 추가
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  # 추가
from django.views.generic import DetailView


def tube_list(request):
    # 검색 q가 있을 경우 title과 content에서 해당 내용이 있는지 검색
    q = request.GET.get("q", "")
    if q:
        posts = Post.objects.filter(title__contains=q) | Post.objects.filter(
            content__contains=q
        )
        return render(request, "tube/tube_list.html", {"posts": posts, "q": q})
    posts = Post.objects.all()
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    is_subscribed = False  # 구독 여부를 확인하는 변수 초기화
    if request.user.is_authenticated:
        # 현재 사용자가 이 포스트의 저자를 구독하고 있는지 확인
        is_subscribed = Subscription.objects.filter(
            subscriber=request.user, channel=post.author
        ).exists()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    if request.method == "GET":
        post.view_count += 1
        post.save()
    return render(
        request,
        "tube/tube_detail.html",
        {"post": post, "form": form, "is_subscribed": is_subscribed},
    )


@login_required
def tube_create(request):
    if request.method == "GET":
        form = PostForm()
        context = {"form": form}
        return render(request, "tube/tube_create.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("tube_list")
        else:
            context = {"form": form}
            return render(request, "tube/tube_create.html", context)


@login_required
def tube_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 내가 쓴 게시물만 업데이트 가능
    if post.author != request.user:
        return redirect("tube_list")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("tube_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
        context = {"form": form, "pk": pk}
        return render(request, "tube/tube_update.html", context)


@login_required
def tube_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 내가 쓴 게시물만 삭제 가능
    if post.author != request.user:
        return redirect("tube_list")

    if request.method == "POST":
        post.delete()
    return redirect("tube_list")


def tube_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("tube_detail", post_pk)


@login_required
def tube_subscribe(request, post_id, user_id):
    """구독 추가 뷰"""
    user = request.user  # 현재 로그인한 사용자
    channel = get_object_or_404(User, pk=user_id)  # 구독할 채널(사용자)

    # 이미 구독한 경우 추가하지 않습니다.
    if Subscription.objects.filter(subscriber=user, channel=channel).exists():
        return redirect("tube_detail", pk=post_id)

    # 구독 객체 생성
    q = Subscription.objects.create(subscriber=user, channel=channel)
    q.save()

    return redirect("tube_detail", pk=post_id)


@login_required
def tube_unsubscribe(request, post_id, user_id):
    """구독 취소 뷰"""
    user = request.user  # 현재 로그인한 사용자
    channel = get_object_or_404(User, pk=user_id)  # 구독 취소할 채널(사용자)

    # 구독 객체가 존재하면 삭제합니다.
    Subscription.objects.filter(subscriber=user, channel=channel).delete()
    return redirect("tube_detail", pk=post_id)


# class PostDetailView(DetailView):
#     model = Post
#     # context_object_name = 'licat_objects' # {{licat_objects.title}} 이런식으로 사용 가능

#     def get_context_data(self, **kwargs):
#         """
#         여기서 원하는 쿼리셋이나 object를 추가한 후 템플릿으로 전달할 수 있습니다.
#         """
#         context = super().get_context_data(**kwargs)
#         print("------------")
#         print(kwargs)
#         print(context)
#         print(type(context))
#         print(dir(context))
#         print("------------")
#         return context


# post_detail2 = PostDetailView.as_view()
