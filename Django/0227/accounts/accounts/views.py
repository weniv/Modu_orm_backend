from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/form.html",
    success_url=settings.LOGIN_URL,
)


login = LoginView.as_view(
    template_name="accounts/form.html",
    # success_url=settings.LOGIN_REDIRECT_URL,
    # next_page=settings.LOGIN_REDIRECT_URL,
)


logout = LogoutView.as_view(
    next_page=settings.LOGOUT_URL,
)


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def logincheck(request):
    print(request.user.is_authenticated)
    print(request.user)
    print(type(request.user))
    print(dir(request.user))
    return render(request, "accounts/logincheck.html")


def loginfbv(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        print(type(user))
        if user is not None:
            login(request, user)
            return HttpResponse("login 성공")
        else:
            return HttpResponse("login 실패")
    return render(request, "accounts/loginfbv.html")
