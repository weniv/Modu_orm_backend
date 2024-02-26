from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    main_image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)
    # 아래처럼 upload_to를 함수로 지정할 수도 있습니다.
    # 이미지 중복되면 이미지에는 난수 들어가니 걱정하시지 않으셔도 됩니다.
    # 이미지가 하나의 폴더에 많아졌을 경우, 성능이슈가 있을 수 있습니다. 그래서 폴더 분리를 권장합니다.

    # a.png => 2021/02/26/123456789.png 이렇게 되어 있어야 언제 업로드 되었는지 알 수 있습니다.
    # DB에서 게시물 생성 날짜로 알 수 있습니다.
    # 1. 만약에 이미 a.png라고 저장이 되어있다면 자동화 스크립트를 만들어서 DB에서 게시물 생성 날짜를 가져와서 파일명을 재작성하는 방법
    # 2. 만약에 이미 a.png라고 저장이 되어있다면 일관된 날짜로(서비스 시작 날짜)로 폴더를 만들어서 그 안에 넣는 방법

    # 아니면 filename에 날짜를 넣는 것도 좋은 방법입니다.
    # 난수로 처리하면 보안성은 올라가지만 파일명을 알 수 없어서 관리가 어려울 수 있습니다.
    # def get_image_path(instance, filename):
    #     return f"blog/{instance.pk}/%Y/%m/{filename}"
    # main_image = models.ImageField(upload_to=get_image_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성될 때만 추가
    updated_at = models.DateTimeField(auto_now=True)  # 수정할 때마다 추가

    def __str__(self):
        return self.title
