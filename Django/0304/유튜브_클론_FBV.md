# 기본 요구사항

/tube   
/tube/1                     # 영상 재생이 되어야 합니다. 뎃글을 달 수 있어야 합니다.
/tube/create/               # 로그인한 사용자만 보기 가능
/tube/update/<int:pk>/      # 로그인한 사용자만 보기 가능, 자신의 글만 업데이트 가능.(자신의 글에서 수정하기 버튼 노출)
/tube/delete/<int:pk>/      # 로그인한 사용자만 보기 가능, 자신의 글만 삭제 가능.(자신의 글에서 삭제하기 버튼 노출)
/tube/tag/<str:tag>/        # 해당 태그가 달린 목록을 가져와야 합니다.
/tube/?q='keyword'          # 해당 키워드가 포함된 title, content가 있는 목록을 가져와야 합니다.
/accounts/signup/
/accounts/login/
/accounts/logout/           # 로그인한 사용자만 보기 가능
/accounts/profile/          # 로그인한 사용자만 보기 가능

# 기획
* 기획은 아래와 같이 정리하시길 권해드립니다.
    * 링크: https://github.com/weniv/project_sample_repo
* 디자인은 아래 폴더에 django_youtube_clone_asset 에 있습니다. 가지고 있는 이미지를 사용하셔도 됩니다.
    * https://github.com/weniv/weniv_friends_design_asset


# 구현단계
* part1 ~ part4까지 구현하시고, part5 부터는 복잡도가 올라가기에 선택사항으로 두겠습니다.
* part1: (기본) 프로젝트 생성 및 기본 세팅
* part2: (기본) 로그인한 사용자만 create, update, delete 구현
* part3: (기본) 검색 기능 구현
* part4: (기본) 템플릿 상속
* part5: UI 꾸미기, 조회수 표시, 뎃글 삭제 기능 추가
* part6: 구독 기능 추가

# 명령어
```python

###################################

# part1 프로젝트 생성 및 기본 세팅

###################################

mkdir tube
cd tube
python -m venv venv
.\venv\Scripts\activate
pip install django
pip install pillow
django-admin startproject config .
pip freeze > requirements.txt
python manage.py migrate
python manage.py startapp accounts
python manage.py startapp tube

###################################
# settings.py

# settings.py에서 접속할 수 있는 사람 설정
ALLOWED_HOSTS = ['*'] # 28번째 줄에 접속할 수 있는 사람을 모든 사람으로 변경

# settings.py 에서 33번째 라인 수정
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'tube',
]

# 중략

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 중략

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

###################################
# mysite > media 폴더 생성
# mysite > static 폴더 생성
# mysite > templates 폴더 생성

mkdir static
mkdir media
mkdir templates

###################################
# tube > models.py

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/")
    video_file = models.FileField(upload_to="blog/files/%Y/%m/%d/")
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


###################################
# tube > admin.py

from django.contrib import admin
from .models import Post, Comment, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)

###################################

python manage.py makemigrations
python manage.py migrate

###################################

python manage.py createsuperuser

leehojun
leehojun@gmail.com
이호준1234!

###################################

python manage.py runserver

썸네일과 영상 포함한 게시물 3개 업로드!

###################################
# config > urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tube/", include("tube.urls")),
    path("accounts/", include("accounts.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###################################
# tube > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.tube_list, name="tube_list"),
    path("<int:pk>/", views.tube_detail, name="tube_detail"),
    path("create/", views.tube_create, name="tube_create"),
    path("<int:pk>/update/", views.tube_update, name="tube_update"),
    path("<int:pk>/delete/", views.tube_delete, name="tube_delete"),
    path("tag/<str:tag>/", views.tube_tag, name="tube_tag"),
]

###################################
# tube > views.py

from django.shortcuts import render
from .models import Post, Comment, Tag
from .forms import CommentForm


def tube_list(request):
    posts = Post.objects.all()
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, "tube/tube_detail.html", {"post": post, "form": form})


def tube_create(request):
    pass


def tube_update(request, pk):
    pass


def tube_delete(request, pk):
    pass


def tube_tag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, "tube/tube_list.html", {"posts": posts})



###################################
# forms.py
from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


###################################

templates > tube > tube_list.html
templates > tube > tube_detail.html

###################################
# templates > tube > tube_list.html

{% for post in posts %}
    <!-- 클랙했을 때 해당 게시물로 이동 -->
    <a href="{% url 'tube_detail' post.pk %}">
        <h1>{{ post.title }}</h1>
        <!-- 썸네일 이미지가 있는지 확인 후 로드 -->
        {% if post.thumbnail_image %}
        <img src="{{ post.thumbnail_image.url }}" alt="{{ post.title }}">
        {% endif %}
        <!-- 조회수와 업로드 날짜 -->
        <!-- ㄱ 하고 한자 눌러 단축키 입력하세요. -->
        <p>{{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
        <p>{{ post.author }}</p>
    </a>
    <hr>
{% endfor %}

###################################
# templates > blog > tube_detail.html

<h1>{{ post.title }}</h1>
<p>{{ post.author }}</p>
<p>{{ post.content|linebreaks }}</p>

<video controls>
    <source src="{{ post.video_file.url }}"></source>      
</video>

{% for tag in post.tags.all %}
    <a href="/tube/tag/{{ tag.name }}">#{{ tag.name }}</a>
{% endfor %}

{% for comment in post.comments.all %}
    <p>{{ comment.message }}</p>
{% endfor %}

<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>

###################################
# accounts에 url이 없기 때문에 지금 돌아가지 않습니다.
# 만약 돌아가게 하고 싶으면 아래 urls.py 잠시 비워두고 실행시키세요.

python manage.py runserver

###################################
# account > urls.py
from django.urls import path
from . import views

# login, logout 이름 사용 X

urlpatterns = [
    path("signup/", views.user_signup, name="user_signup"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("profile/", views.user_profile, name="user_profile"),
]


###################################
# account > views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def user_signup(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST.get("email", "")

        if not (username and password):
            return HttpResponse("이름과 패스워드는 필수입니다.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("유저이름이 이미 있습니다.")
        if email and User.objects.filter(email=email).exists():
            return HttpResponse("이메일이 이미 있습니다.")

        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("user_profile")
    else:
        return render(request, "accounts/signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_profile")
        else:
            return render(request, "accounts/login.html")
    else:
        return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("user_login")


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})


###################################
# accounts > login.html

<form method="post">
    {% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">로그인</button>
</form>

###################################
# accounts > signup.html

<form action="" method="post">
    {% csrf_token %}
    <label for="username_id">아이디</label>
    <input id="username_id" type="text" name="username">

    <label for="email_id">이메일</label>
    <input id="email_id" type="text" name="email">
    
    <label for="password_id">비밀번호</label>
    <input id="password_id" type="password" name="password">
    
    <button type="submit">회원가입</button>
</form>

###################################
# accounts > profile.html


<h1>개인 프로필 페이지</h1>
<p>{{ user }}</p>
<p>{{ user.is_authenticated }}</p>
<p>{{ user.username }}</p>
<p>{{ user.email }}</p>
<p>{{ user.first_name }}</p>
<p>{{ user.last_name }}</p>
<p>{{ user.is_staff }}</p>
<p>{{ user.is_active }}</p>
<p>{{ user.is_superuser }}</p>
<p>{{ user.last_login }}</p>
<p>{{ user.date_joined }}</p>

<form action="{% url 'user_logout' %}" method="post">
    {% csrf_token %}
    <input type="submit" value="로그아웃">
</form>

###################################

python manage.py runserver

http://127.0.0.1:8000/tube/
http://127.0.0.1:8000/tube/1/
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/profile/ # 로그아웃된 상태에서 접속되는지 확인
http://127.0.0.1:8000/accounts/signup/

###################################

# part2 로그인한 사용자만 create, update, delete 구현

###################################
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Tag
from .forms import CommentForm, PostForm


def tube_list(request):
    posts = Post.objects.all()
    return render(request, "tube/tube_list.html", {"posts": posts})


def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    return render(request, "tube/tube_detail.html", {"post": post, "form": form})


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


###################################
# forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

###################################
# tube_create.html, tube_update.html

<form action="" method="post">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit">
</form>


###################################
# tube_detail.html

<h1>{{ post.title }}</h1>
<p>{{ post.author }}</p>
<p>{{ post.content|linebreaks }}</p>

<video controls>
    <source src="{{ post.video_file.url }}"></source>      
</video>

<!-- 로그인을 했고, 내가 이 글에 글쓴이라고 한다면 삭제와 업데이트 버튼 노출 -->
{% if user.is_authenticated and user == post.author %}
    <a href="{% url 'tube_update' post.pk %}">수정</a>
    <form action="{% url 'tube_delete' post.pk %}" method="post">
        {% csrf_token %}
        <input type="submit" value="삭제">
    </form>
{% endif %}

{% for tag in post.tags.all %}
    <a href="/tube/tag/{{ tag.name }}">#{{ tag.name }}</a>
{% endfor %}

{% for comment in post.comments.all %}
    <p>{{ comment.message }}</p>
{% endfor %}

<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>


###################################

test

http://127.0.0.1:8000/tube/
http://127.0.0.1:8000/tube/
http://127.0.0.1:8000/tube/1/
http://127.0.0.1:8000/tube/1/update/ # 업데이트 확인
http://127.0.0.1:8000/tube/1/ # 삭제 확인


###################################

# part3 검색 기능 구현

###################################
# tube_list.html

<form action="" method="get">
    <input type="text" name="q" value="{{ request.GET.q }}">
    <input type="submit" value="검색">
</form>

{% for post in posts %}
    <!-- 클랙했을 때 해당 게시물로 이동 -->
    <a href="{% url 'tube_detail' post.pk %}">
        <h1>{{ post.title }}</h1>
        <!-- 썸네일 이미지가 있는지 확인 후 로드 -->
        {% if post.thumbnail_image %}
        <img src="{{ post.thumbnail_image.url }}" alt="{{ post.title }}">
        {% endif %}
        <!-- 조회수와 업로드 날짜 -->
        <!-- ㄱ 하고 한자 눌러 단축키 입력하세요. -->
        <p>{{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
        <p>{{ post.author }}</p>
        <!-- 태그 추가 -->
        {% for tag in post.tags.all %}
            <a href="{% url 'tube_tag' tag.name %}">{{ tag.name }}</a>
        {% endfor %}
    </a>
    <hr>
{% endfor %}
###################################
# views.py

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

###################################

# part4 템플릿 상속

###################################
# templates > base.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>tube 클론</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{% url 'tube_list' %}">tube</a></li>
                {% if user.is_authenticated %}
                    <li><a href="{% url 'tube_create' %}">글쓰기</a></li>
                    <li><a href="{% url 'user_profile' %}">프로필</a></li>
                    <li><a href="{% url 'user_logout' %}">로그아웃</a></li>
                {% else %}
                    <li><a href="{% url 'user_login' %}">로그인</a></li>
                    <li><a href="{% url 'user_signup' %}">회원가입</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>
    <form action="" method="get">
        <input type="text" name="q" value="{{ request.GET.q }}">
        <input type="submit" value="검색">
    </form>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

###################################
# tube_list.html

{% extends 'base.html' %}
{% block content %}
{% for post in posts %}
    <!-- 클랙했을 때 해당 게시물로 이동 -->
    <a href="{% url 'tube_detail' post.pk %}">
        <h1>{{ post.title }}</h1>
        <!-- 썸네일 이미지가 있는지 확인 후 로드 -->
        {% if post.thumbnail_image %}
        <img src="{{ post.thumbnail_image.url }}" alt="{{ post.title }}">
        {% endif %}
        <!-- 조회수와 업로드 날짜 -->
        <!-- ㄱ 하고 한자 눌러 단축키 입력하세요. -->
        <p>{{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
        <p>{{ post.author }}</p>
        <!-- 태그 추가 -->
        {% for tag in post.tags.all %}
            <a href="{% url 'tube_tag' tag.name %}">{{ tag.name }}</a>
        {% endfor %}
    </a>
{% endfor %}
{% endblock %}

###################################
# tube_detail.html

{% extends 'base.html' %}
{% block content %}
<h2>{{ post.title }}</h2>
<p>{{ post.author }}</p>
<p>{{ post.content|linebreaks }}</p>

<video controls>
    <source src="{{ post.video_file.url }}"></source>      
</video>

<!-- 로그인을 했고, 내가 이 글에 글쓴이라고 한다면 삭제와 업데이트 버튼 노출 -->
{% if user.is_authenticated and user == post.author %}
    <a href="{% url 'tube_update' post.pk %}">수정</a>
    <form action="{% url 'tube_delete' post.pk %}" method="post">
        {% csrf_token %}
        <input type="submit" value="삭제">
    </form>
{% endif %}

{% for tag in post.tags.all %}
    <a href="/tube/tag/{{ tag.name }}">#{{ tag.name }}</a>
{% endfor %}

{% for comment in post.comments.all %}
    <p>{{ comment.message }}</p>
{% endfor %}

<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
{% endblock %}

###################################

# part5 UI 꾸미기, 조회수 표시, 뎃글 삭제 기능 추가

###################################

# 수업에서는 설치형을 쓰지 않고 cdn을 사용합니다.
# 사용법은 https://pypi.org/project/django-tailwindcss/ 를 참고하세요.

pip install django-tailwindcss

###################################
# base.html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tube 클론</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <header class="py-2 flex justify-around items-center border-b border-gray-300">
        <h1 class="text-xl font-bold"><a href="{% url 'tube_list' %}">Tube</a></h1>
        <form action="" method="get">
            <input class="border border-gray-300 rounded-xl px-4 py-[5px] text-xs" type="text" name="q" value="{{ request.GET.q }}">
            <input class="bg-blue-200 text-white rounded px-2 py-[5px] text-xs" type="submit" value="검색">
        </form>
        <nav>
            <ul class="flex justify-end gap-2">
                {% if user.is_authenticated %}
                    <li class="inline-block ml-3 border border-gray-300 rounded px-2 py-[5px] text-xs"><a href="{% url 'tube_create' %}">글쓰기</a></li>
                    <li class="inline-block ml-3 border border-gray-300 rounded px-2 py-[5px] text-xs"><a href="{% url 'user_profile' %}">프로필</a></li>
                {% else %}
                    <li class="inline-block ml-3 border border-gray-300 rounded px-2 py-[5px] text-xs"><a href="{% url 'user_login' %}">로그인</a></li>
                    <li class="inline-block ml-3 border border-gray-300 rounded px-2 py-[5px] text-xs"><a href="{% url 'user_signup' %}">회원가입</a></li>
                {% endif %}
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>


###################################
# tube_list.html
{% extends 'base.html' %}
{% block content %}
<div class="grid grid-cols-4 gap-4 p-4 m-6">
{% for post in posts %}
    <section>
        <!-- 클랙했을 때 해당 게시물로 이동 -->
        <a href="{% url 'tube_detail' post.pk %}">
            <!-- 썸네일 이미지가 있는지 확인 후 로드 -->
            {% if post.thumbnail_image %}
                <img class="w-[100%] rounded-lg" src="{{ post.thumbnail_image.url }}" alt="{{ post.title }}">
            {% endif %}
            <h2 class="font-bold">{{ post.title }}</h2>
            <!-- 조회수와 업로드 날짜 -->
            <!-- ㄱ 하고 한자 눌러 단축키 입력하세요. -->
            <p>조회수 {{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
            <p>{{ post.author }}</p>
            <!-- 태그 추가 -->
            {% for tag in post.tags.all %}
                <a href="{% url 'tube_tag' tag.name %}">{{ tag.name }}</a>
            {% endfor %}
        </a>
    </section>
{% endfor %}
</div>
{% endblock %}

###################################
# tube_detail.html

{% extends 'base.html' %}
{% block content %}
<section class="detail-container m-6 space-y-4">
    
    <video class="w-100" controls>
        <source src="{{ post.video_file.url }}"></source>      
    </video>

    <h2 class="font-bold text-xl">{{ post.title }}</h2>
    <p>{{ post.author }}</p>
    <div class="bg-gray-200 p-4 rounded-lg text-sm">
        <p>조회수 {{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
        {{ post.content|linebreaks }}
    </div>

    {% for tag in post.tags.all %}
        <a class="text-blue-600" href="/tube/tag/{{ tag.name }}">#{{ tag.name }}</a>
    {% endfor %}

    <!-- 로그인을 했고, 내가 이 글에 글쓴이라고 한다면 삭제와 업데이트 버튼 노출 -->
    {% if user.is_authenticated and user == post.author %}
    <div class="flex gap-4">
        <a class="border border-gray-200 p-2 rounded-lg" href="{% url 'tube_update' post.pk %}">수정</a>
        <form class="border border-gray-200 p-2 rounded-lg" action="{% url 'tube_delete' post.pk %}" method="post">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
    </div>
    {% endif %}

    <p class="font-bold text-xl">댓글 {{ post.comments.count }}개</p>
    <form action="" method="post" class="flex p-4 space-y-4 space-x-2 bg-white shadow-md rounded-lg">
        {% csrf_token %}
        <div class="flex w-20 items-center justify-center">
            <label for="id_message" class="text-sm font-medium text-gray-700 text-center">뎃글 작성:</label>
        </div>
        
        <textarea name="message" cols="40" required="" id="id_message" class="mt-1 block w-3/4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
        <input type="submit" value="작성" class="py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
    </form>
    
    {% for comment in post.comments.all %}
        <div class="border border-gray-200 p-4 rounded-lg">
            <p><span class="font-bold">{{ comment.author }}</span> · {{ comment.created_at|timesince }} 전</p>
            <p>{{ comment.message }}</p>
            {% if user.is_authenticated and user == comment.author %}
            <div class="flex gap-4">
                <form class="" action="{% url 'tube_comment_delete' comment.pk %}" method="post">
                    {% csrf_token %}
                    <input class="text-gray-500 hover:text-gray-800 text-sm" type="submit" value="삭제">
                </form>
            </div>
            {% endif %}
        </div>
    {% endfor %}
</section>
{% endblock %}

###################################
# tube > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.tube_list, name="tube_list"),
    path("<int:pk>/", views.tube_detail, name="tube_detail"),
    path("create/", views.tube_create, name="tube_create"),
    path("<int:pk>/update/", views.tube_update, name="tube_update"),
    path("<int:pk>/delete/", views.tube_delete, name="tube_delete"),
    path("tag/<str:tag>/", views.tube_tag, name="tube_tag"),
    # comment 삭제 url 추가
    path("<int:pk>/comment_delete/", views.tube_comment_delete, name="tube_comment_delete"),
]


###################################
# views.py

def tube_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
    if request.method == "GET": # count 수정
        post.view_count += 1
        post.save()
    return render(request, "tube/tube_detail.html", {"post": post, "form": form})


def tube_comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("tube_detail", post_pk)

###################################

# part6 구독 기능 추가

###################################
#  tube > models.py

class Subscription(models.Model):
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    channel = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribers"
    )
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("subscriber", "channel")  # 구독자와 채널은 유일해야 함

    def __str__(self):
        return f"{self.subscriber.username}이 {self.channel.username}를 구독하였습니다."

###################################

python manage.py makemigrations
python manage.py migrate

###################################

from django.contrib import admin
from .models import Post, Comment, Tag, Subscription

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Subscription)


###################################
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.tube_list, name="tube_list"),
    path("<int:pk>/", views.tube_detail, name="tube_detail"),
    path("create/", views.tube_create, name="tube_create"),
    path("<int:pk>/update/", views.tube_update, name="tube_update"),
    path("<int:pk>/delete/", views.tube_delete, name="tube_delete"),
    path("tag/<str:tag>/", views.tube_tag, name="tube_tag"),
    # comment 삭제 url 추가
    path(
        "<int:pk>/comment_delete/",
        views.tube_comment_delete,
        name="tube_comment_delete",
    ),
    # 구독 url 추가
    path(
        "<int:post_id>/<int:user_id>/subscribe/",
        views.tube_subscribe,
        name="tube_subscribe",
    ),
    # 구독 취소 url 추가
    path(
        "<int:post_id>/<int:user_id>/unsubscribe/",
        views.tube_unsubscribe,
        name="tube_unsubscribe",
    ),
]



###################################
# views.py

from django.shortcuts import render, redirect
from .models import Post, Comment, Tag, Subscription  # 추가
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  # 추가


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



###################################
# tube_detail.html

{% extends 'base.html' %}
{% block content %}
<section class="detail-container m-6 space-y-4">
    
    <video class="w-100" controls>
        <source src="{{ post.video_file.url }}"></source>      
    </video>

    <h2 class="font-bold text-xl">{{ post.title }}</h2>
    <p>{{ post.author }}</p>

    <!-- 구독을 했을 경우 구독중 버튼을 구독을 안했을 경우 구독 버튼을 노출-->
    {% if user.is_authenticated and user != post.author %}
        {# {{ post.author.subscribers.all }}를 그냥 순회돌면 쿼리셋입니다. #}
        {% if is_subscribed %}
            <form action="{% url 'tube_unsubscribe' post.pk post.author.pk %}" method="post">
                {% csrf_token %}
                <input type="submit" value="구독중" class="border border-gray-200 p-2 rounded-lg">
            </form>
        {% else %}
            <form action="{% url 'tube_subscribe' post.pk post.author.pk %}" method="post">
                {% csrf_token %}
                <input type="submit" value="구독" class="border border-gray-200 p-2 rounded-lg">
            </form>
        {% endif %}
    {% endif %}

    <div class="bg-gray-200 p-4 rounded-lg text-sm">
        <p>조회수 {{ post.view_count }}회 · {{ post.created_at|timesince }} 전</p>
        {{ post.content|linebreaks }}
    </div>

    {% for tag in post.tags.all %}
        <a class="text-blue-600" href="/tube/tag/{{ tag.name }}">#{{ tag.name }}</a>
    {% endfor %}

    <!-- 로그인을 했고, 내가 이 글에 글쓴이라고 한다면 삭제와 업데이트 버튼 노출 -->
    {% if user.is_authenticated and user == post.author %}
    <div class="flex gap-4">
        <a class="border border-gray-200 p-2 rounded-lg" href="{% url 'tube_update' post.pk %}">수정</a>
        <form class="border border-gray-200 p-2 rounded-lg" action="{% url 'tube_delete' post.pk %}" method="post">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
    </div>
    {% endif %}

    <p class="font-bold text-xl">댓글 {{ post.comments.count }}개</p>
    <form action="" method="post" class="flex p-4 space-y-4 space-x-2 bg-white shadow-md rounded-lg">
        {% csrf_token %}
        <div class="flex w-20 items-center justify-center">
            <label for="id_message" class="text-sm font-medium text-gray-700 text-center">뎃글 작성:</label>
        </div>
        
        <textarea name="message" cols="40" required="" id="id_message" class="mt-1 block w-3/4 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
        <input type="submit" value="작성" class="py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
    </form>
    
    {% for comment in post.comments.all %}
        <div class="border border-gray-200 p-4 rounded-lg">
            <p><span class="font-bold">{{ comment.author }}</span> · {{ comment.created_at|timesince }} 전</p>
            <p>{{ comment.message }}</p>
            {% if user.is_authenticated and user == comment.author %}
            <div class="flex gap-4">
                <form class="" action="{% url 'tube_comment_delete' comment.pk %}" method="post">
                    {% csrf_token %}
                    <input class="text-gray-500 hover:text-gray-800 text-sm" type="submit" value="삭제">
                </form>
            </div>
            {% endif %}
        </div>
    {% endfor %}
</section>
{% endblock %}
###################################
```