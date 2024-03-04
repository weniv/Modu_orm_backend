from django.urls import path
from . import views

urlpatterns = [
    path("", views.tube_list, name="tube_list"),
    path("<int:pk>/", views.tube_detail, name="tube_detail"),
    # path("<int:pk>/", views.post_detail2, name="post_detail2"),
    path("create/", views.tube_create, name="tube_create"),
    path("<int:pk>/update/", views.tube_update, name="tube_update"),
    path("<int:pk>/delete/", views.tube_delete, name="tube_delete"),
    path("tag/<str:tag>/", views.tube_tag, name="tube_tag"),
    # comment 삭제 url 추가
    path(
        "<int:pk>/comment_delete/",
        views.tube_comment_delete,
        name="tube_comment_delete",
    ),
    # 구독 url 추가
    path(
        "<int:post_id>/<int:user_id>/subscribe/",
        views.tube_subscribe,
        name="tube_subscribe",
    ),
    # 구독 취소 url 추가
    path(
        "<int:post_id>/<int:user_id>/unsubscribe/",
        views.tube_unsubscribe,
        name="tube_unsubscribe",
    ),
]
