from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("Blog Page")


def blogdetails(request, pk):
    return HttpResponse(f"Blog Details Page: {pk}")
