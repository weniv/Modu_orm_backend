# modeling_tip/005.py
# 모델 매니저를 활용하여 자주 사용하는 쿼리를 간편하게 정의할 수 있습니다.
# Post.objects.published()와 같이 커스텀 매니저에 정의된 메서드를 사용할 수 있게 됩니다.
# 자주 사용되는 쿼리나 복잡한 쿼리 로직을 모델 매니저에 추상화하고, 이를 통해 코드의 중복을 줄이고 가독성을 높일 수 있습니다.


class PostManager(models.Manager):
    def published(self):
        return self.filter(status=Post.StatusChoices.PUBLISHED)


class Post(models.Model):
    # ...
    objects = PostManager()
