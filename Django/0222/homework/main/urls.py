from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, world! index")),
    path("about/", lambda request: HttpResponse("Hello, world! about")),
]
