from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<int:pk>/", views.blog_details, name="blog_details"),
    path("create/", views.blog_create, name="blog_create"),
    path("update/<int:pk>/", views.blog_update, name="blog_update"),
    path("delete/<int:pk>/", views.blog_delete, name="blog_delete"),
]
