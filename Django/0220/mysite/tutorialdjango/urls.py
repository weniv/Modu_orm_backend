from django.contrib import admin
from django.urls import path
from main.views import index, a, b, c, hojun, orm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("a/", a),
    path("b/", b),
    path("c/", c),
    path("hojun/", hojun),
    path("orm/", orm),
]
