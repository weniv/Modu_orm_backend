from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.notice_list, name="notice_list"),
    path("post/<int:pk>/", views.notice_detail, name="notice_detail"),
]
