from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView


class TubeSignupView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/form.html"
    success_url = settings.LOGIN_URL


signup = TubeSignupView.as_view()


class TubeLoginView(LoginView):
    template_name = "accounts/form.html"


login = TubeLoginView.as_view()


class TubeLogoutView(LogoutView):
    next_page = settings.LOGIN_URL


logout = TubeLogoutView.as_view()


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
