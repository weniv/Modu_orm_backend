from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    # ""URL로 들어오면 main앱에 urls.py로 연결하겠다.
    # path('', index),
    # path('about/', about),
    # path('contact/', contact),
    path("blog/", include("blog.urls")),
    # "blog/"URL로 들어오면 blog앱에 urls.py로 연결하겠다.
    # path("blog/<int:pk>/", blogdetails), # 여기서 처리하지 않고 blog앱에 urls.py에서 처리하면 됩니다!
    # path('blog/', blog),
    # path('blog/1', blog_1),
    # path('blog/2', blog_2),
    # path('blog/3', blog_3),
    path("accounts/", include("accounts.urls")),
    # path('accounts/login', login),
    # path('accounts/logout', logout),
]
