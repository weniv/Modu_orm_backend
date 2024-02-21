import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse


blog_list = [
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "자바스크립트는 별로였어!!!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list = [
    {
        "id": 1,
        "username": "hojun",
        "email": "hojun@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]


def index(request):
    return render(request, "main/index.html")


def bloglist(request):
    context = {"blogitems": blog_list}
    return render(request, "main/bloglist.html", context)


def blogdetails(request, pk):
    blog = blog_list[pk - 1]
    language = ["html", "css", "js", "python"]
    context = {"blog": blog, "language": language}
    return render(request, "main/blogdetails.html", context)


def userdetails(request, user):
    finduser = None
    for i in user_list:
        if i["username"] == user:
            finduser = i
    if finduser is None:
        return render(request, "main/notfound.html")
    return render(request, "main/userdetails.html", {"user": finduser})


def bookinfo(request):

    url = "https://paullab.co.kr/bookservice/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select("h2")
    bookcover = soup.select(".book_cover")

    result = []

    for title, cover in zip(titles, bookcover):
        result.append((title.text, "https://paullab.co.kr/bookservice/" + cover["src"]))

    return render(request, "main/bookinfo.html", {"bookinfo": result})
