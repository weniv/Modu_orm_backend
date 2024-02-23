from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("create/<str:title>/", views.blog_create, name="blog_create"),
    path("delete/<int:pk>/", views.blog_delete, name="blog_delete"),
    path("test/", views.blog_test, name="test"),
]
