# 목표
1. 아주 간단한 DB를 다뤄봅니다. 25분동안!

# django
```python

# 상위 폴더로 올라와서 하셔야 합니다.


mkdir db
cd db
python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject tutorialdjango .
python manage.py migrate
python manage.py startapp main
python manage.py startapp blog

################################
# tutorialdjango > settings.py

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "blog",
]

################################

# URL 구조 작성(기획 단계), 연습할 때에도 이걸 만들어놓고 연습하시기를 권고합니다.

''
'blog/'
'blog/<int:pk>/'

앱이름: main
URL             views 함수이름	 html 파일이름	    비고
''              index           

앱이름: blog
URL             views 함수이름   html 파일이름      비고
'blog/'         blog            blog.html	
'blog/<int:pk>' post            post.html          게시물이 없을 경우에는 404로 연결

################################
# tutorialdjango > urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("blog/", include("blog.urls")),
]

################################
# main > urls.py

from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, world!")),
]

################################
# blog > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]


################################
# blog > views.py

from django.shortcuts import render


def blog_list(request):
    return render(request, "blog_list.html")


def blog_detail(request, pk):
    return render(request, "blog_detail.html")



################################
# 아래 파일들 생성

templates > blog_list.html
templates > blog_detail.html


################################
# blog > models.py
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
# 어떤 항목을 게시판에 게시할지 기획 => 기획된 항목들이 어떤 타입인지 ref 문서에서 확인

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

################################

python manage.py makemigrations # 파이썬 코드로 DB를 만질 수 있는 코드를 생성
python manage.py migrate # 위에 생성된 코드로 실제 DB를 만지는 명령

################################

python manage.py createsuperuser
leehojun
leehojun@gmail.com
dlghwns1234!
dlghwns1234!

################################

from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

################################

/admin으로 로그인 후 게시물 3개 작성

################################

# blog > views.py 수정

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



################################
# templates > blog > blog_list.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <h1>bloglist</h1>
    <ul>
        {% for blog in blog_list %}
        <li>
            {{ forloop.counter }}
            {# 주석입니다. 'url 'blog_detail' blog.id' 와 같은 형태는 urls.py에서 blog_detail이라는 name을 가진 url을 찾습니다. 그걸로만 연결을 해주는데 뒤에 값이 들어가야 할 경우, 파라미터가 있는 경우! 뒤에 띄어쓰기로 아규먼트를 넣어줄 수 있습니다. 결국에는 blog.id가 blog_detail에 pk로 들어가는 것입니다. #}
            <a href="{% url 'blog_detail' blog.id %}">{{ blog.title }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

################################
# templates > blog > blog_detail.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>blogdetail</title>
</head>
<body>
    <h1>blogdetail</h1>
    <h2>{{ blog.title }}</h2>
    <p>{{ blog.contents }}</p>
    <p>{{ blog.created_at }}</p>
    <p>{{ blog.updated_at }}</p>
    <a href="{% url 'blog_list' %}">목록</a>
</body>
</html>