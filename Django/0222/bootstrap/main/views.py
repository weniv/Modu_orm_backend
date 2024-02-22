from django.shortcuts import render, redirect


def index(request):
    return redirect("blog_list")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")
