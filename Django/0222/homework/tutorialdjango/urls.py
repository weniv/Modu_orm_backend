from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("product/", include("product.urls")),
    path("qna/", include("qna.urls")),
]
