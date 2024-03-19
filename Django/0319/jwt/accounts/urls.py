from django.contrib import admin
from django.urls import path, include
from .views import example_view

urlpatterns = [
    path("test/", example_view),
    path("join/", include("dj_rest_auth.registration.urls")),
    path("", include("dj_rest_auth.urls")),
]
