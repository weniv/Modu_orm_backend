# modeling_tip/004.py
# choices 옵션을 사용하면 필드의 선택 가능한 옵션을 제한할 수 있습니다.
# 이는 데이터 무결성을 유지하고 잘못된 값이 입력되는 것을 방지합니다.
# 2개를 비교해보겠습니다.
# class 방식은 Django 3.0부터 지원합니다. 이렇게 사용하면 가독성을 개선시키고 일관성을 유지할 수 있습니다.
# 기능상으로는 동일하기에 무조건 어떤 방법으로 해야 한다고 말할 수는 없습니다.


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    # ...


# STATUS_CHOICES를 내부 클래스로 정의하는 예시


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )
    # ...
