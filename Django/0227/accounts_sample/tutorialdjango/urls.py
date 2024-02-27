from django.contrib import admin
from django.urls import path
from accounts.views import index, signup, login, logout, profile

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
]
