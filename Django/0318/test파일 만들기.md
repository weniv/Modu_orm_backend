```python
# blog > test.py
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from blog.models import Post


class BlogTest(TestCase):
    def setUp(self):
        print("-- main app 테스트 BEGIN --")
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="hojun",
            password="dlghwns1234!",
        )
        self.user.save()

        self.blog = Post.objects.create(
            title="test blog title setup",
            content="test blog content setup",
            author=self.user,
        )
        self.blog.save()

        print("-- main app 테스트 END --")

    def test_blog_read(self):
        """
        blog list Read 가능 테스트
        """
        print("-- blog read 테스트 BEGIN --")
        print("-- 비회원 읽기 테스트 --")
        response = self.client.get("/blog/post/")
        self.assertEqual(response.status_code, 403)

        print("-- 회원 읽기 테스트 --")
        self.client.login(username="hojun", password="dlghwns1234!")
        response = self.client.get("/blog/post/")
        self.assertEqual(response.status_code, 200)
        print("--// blog read 테스트 END --")

    def test_blog_create(self):
        """
        blog Create 가능 테스트
        """
        print("-- blog create 테스트 BEGIN --")
        print("-- 비회원 작성 테스트 --")
        response = self.client.post(
            "/blog/post/",
            {
                "title": "test blog title create",
                "content": "test blog content create",
                "author": self.user.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        print("-- 회원 작성 테스트 --")
        self.client.login(username="hojun", password="dlghwns1234!")
        response = self.client.post(
            "/blog/post/",
            {
                "title": "test blog title create",
                "content": "test blog content create",
                "author": self.user.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        posts = Post.objects.all()
        for i in posts:
            print(i.title)
        print("--// blog create 테스트 END --")



########################
# notice > test.py

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from notice.models import Notice as Post


class NoticeTest(TestCase):
    def setUp(self):
        print("-- main app 테스트 BEGIN --")
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="hojun",
            password="dlghwns1234!",
        )
        self.user.save()

        self.notice = Post.objects.create(
            title="test notice title setup",
            content="test notice content setup",
            author=self.user,
        )
        self.notice.save()

        print("-- main app 테스트 END --")

    def test_notice_read(self):
        """
        notice list Read 가능 테스트
        """
        print("-- notice read 테스트 BEGIN --")
        print("-- 비회원 읽기 테스트 --")
        response = self.client.get("/notice/post/")
        self.assertEqual(response.status_code, 200)

    def test_notice_create(self):
        """
        notice Create 가능 테스트
        """
        print("-- notice create 테스트 BEGIN --")
        print("-- 비회원 작성 테스트 --")
        response = self.client.post(
            "/blog/post/",
            {
                "title": "test blog title create",
                "content": "test blog content create",
                "author": self.user.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        print("-- 회원 작성 테스트 --")
        self.client.login(username="hojun", password="dlghwns1234!")
        response = self.client.post(
            "/blog/post/",
            {
                "title": "test blog title create",
                "content": "test blog content create",
                "author": self.user.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        posts = Post.objects.all()
        for i in posts:
            print(i.title)
        print("--// notice create 테스트 END --")

```