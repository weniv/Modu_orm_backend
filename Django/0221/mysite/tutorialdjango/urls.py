from django.contrib import admin
from django.urls import path
from main.views import index, bloglist, blogdetails, userdetails, bookinfo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("blog/", bloglist),
    path("blog/<int:pk>/", blogdetails),
    path("user/<str:user>/", userdetails),
    path("bookinfo/", bookinfo),
]
