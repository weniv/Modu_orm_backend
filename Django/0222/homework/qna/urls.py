from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, world! qna index")),
    path(
        "<int:pk>/", lambda request, pk: HttpResponse("Hello, world! about qna detail")
    ),
]
