from django.shortcuts import render

blog_database = [
    {
        "id": 1,
        "title": "제목1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "author": "홍길동",
        "category": "일상",
        "tag": ["태그1", "태그2"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 3,
        "like_user": [10, 20, 21],
    },
    {
        "id": 2,
        "title": "제목2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "author": "김철수",
        "category": "일기",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 10,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 3,
        "title": "제목3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "author": "이영희",
        "category": "맛집",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 20,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 4,
        "title": "제목4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "author": "박민수",
        "category": "여행",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 30,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
]


def blog_list(request):
    # blogs = Blog.objects.all() # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog_list": blog_database}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"blog": blog_database[pk - 1]}
    return render(request, "blog/blog_detail.html", context)
