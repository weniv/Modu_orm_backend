# modeling_tip/003.py
# unique_together를 설정하면 여러 필드의 조합이 고유해야 합니다.
# 예를 들어, 사용자 모델에서 email과 username 필드의 조합이 고유해야 한다면 다음과 같이 설정할 수 있습니다.
# 제가 앞서 인스타그램 클론 강의할 때 좋아요를 이런 식으로 구현했었죠. 한 사람이 좋아요는 게시물당 1개를 쓸 수 있습니다.


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    # ...

    class Meta:
        unique_together = ["email", "username"]
