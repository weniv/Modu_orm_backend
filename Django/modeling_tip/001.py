# modeling_tip/001.py
# ordering을 설정하면 해당 모델을 조회할 때 정렬 순서를 지정할 수 있습니다.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
