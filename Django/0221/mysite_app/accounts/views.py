from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("Login Page")


def logout(request):
    return HttpResponse("Logout Page")
