from django.urls import path
from .views import login, logout

urlpatterns = [
    path("login/", login),
    path("logout/", logout),
]
