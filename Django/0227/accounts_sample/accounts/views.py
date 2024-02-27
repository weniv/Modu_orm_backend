from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        # 회원가입 처리 로직
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST.get("email", "")  # 이메일은 선택적으로 처리
        if not (username and password):
            return HttpResponse("Username and password are required.")

        # 동일한 사용자 이름이나 이메일을 가진 사용자가 이미 있는지 검사
        if User.objects.filter(username=username).exists():
            return HttpResponse("A user with that username already exists.")
        if email and User.objects.filter(email=email).exists():
            return HttpResponse("A user with that email already exists.")

        # 새 사용자 생성
        user = User.objects.create_user(username, email, password)
        user.save()

        # 그냥 create하면 비밀번호가 암호화되지 않습니다.
        # 암호화 하지 않고 저장을 해버리면 로그인이 안됩니다.(작동을 안합니다.)
        # 아래 주석 처리된 코드는 위의 코드와 동일한 기능을 합니다.
        # user = User(username=username, email=email)
        # user.set_password(password)  # 이렇게 하면 비밀번호가 암호화됩니다.
        # user.save()

        # 자동 로그인 처리
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # 회원가입 후 프로필 페이지로 리다이렉트
            return redirect("profile")
        else:
            return HttpResponse("Authentication failed.")
    else:
        # GET 요청 시 회원가입 폼 페이지 렌더링
        return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 로그인 성공 시 프로필 페이지로 리다이렉트
            return redirect("profile")
        else:
            # 로그인 실패 시, 로그인 폼과 에러 메시지를 다시 렌더링
            return render(
                request, "login.html", {"error": "Invalid username or password"}
            )
    else:
        # GET 요청 시 로그인 폼 페이지 렌더링
        return render(request, "login.html")


def logout(request):
    # 사용자 로그아웃
    logout(request)
    # 로그아웃 후 리다이렉트할 페이지, 예를 들어 로그인 페이지
    return redirect("login")


@login_required
def profile(request):
    # login_required 데코레이터는 사용자가 로그인하지 않은 상태에서 이 페이지에 접근하려고 하면,
    # 설정된 로그인 URL로 리다이렉트합니다.
    return render(request, "profile.html", {"user": request.user})
