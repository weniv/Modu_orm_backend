from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

# 클래스 기반 뷰가 꼭 제네릭 뷰는 아닙니다.
# 클래스로 HttpResponse를 반환하게 하면 그것도 클래스 기반 뷰입니다.
# 실무에서는 클래스 기반 뷰를 제네릭 뷰라고 부르는 경우가 많습니다.
# 제네릭 뷰는 장고에서 제공하는 여러가지 기능을 미리 구현해 놓은 클래스 기반 뷰입니다.


class PostList(ListView):
    model = Post
    ordering = "-pk"
    # 기본값은 최신 게시물이 맨 아래로 가기 때문에 pk를 기준으로 내림차순 정렬
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_list.html

    def get_queryset(self):
        queryset = super().get_queryset()

        # request에서 GET 파라미터 q를 가져옴
        q = self.request.GET.get("q", "")

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            ).distinct()
        return queryset


class PostDetail(DetailView):
    model = Post
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_detail.html


class PostCreate(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog_list")
    # fields = ["title", "content", "image"]
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html
    # reverse_lazy("blog_list")를 하는 이유는 object가 생성이 되고 나서 url로 이동해야 하는데 reverse는 함수이기 때문에 함수가 실행되는 시점에 url로 이동하게 되어버린다. 그래서 post가 생성된 후에 url로 이동하게 하기 위해서 기다리겠다는 함수가 reverse_lazy를 사용한다.


class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog_list")
    # fields = ["title", "content", "image"]
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_form.html


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("blog_list")
    # 삭제되고 다 완료되지 않은 상태에서 blog_list로 넘어가지 않도록 하기 위해서 reverse_lazy를 사용합니다.
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_confirm_delete.html


class PostTest(CreateView):
    model = Post

    # 이렇게 재정의 하는 것을? 매서드 오버라이딩이라고 합니다.
    def get(self, request):
        return HttpResponse("get 요청이 왔습니다.")

    def post(self, request):
        return HttpResponse("post 요청이 왔습니다.")


# 실무에서는 바로 as_view()를 붙여서 사용합니다.
# urls의 패턴을 우리가 배운 형태되로 유지하기 위해서 아래처럼 사용하겠습니다.
blog_list = PostList.as_view()
blog_details = PostDetail.as_view()
blog_write = PostCreate.as_view()
blog_edit = PostUpdate.as_view()
blog_delete = PostDelete.as_view()
test = PostTest.as_view()
