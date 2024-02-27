from django.urls import path
from .views import blog_list, blog_details

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("<int:pk>/", blog_details, name="blog_details"),
]
