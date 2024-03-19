# modeling_tip/012.py
# 모델 인스턴스를 삭제하는 대신 비활성화하는 방식을 사용할 수 있습니다.


class Post(models.Model):
    # ...
    is_active = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
