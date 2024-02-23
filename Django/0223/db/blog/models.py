from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성될 때에만
    updated_at = models.DateTimeField(auto_now=True)  # 수정될 때마다

    def __str__(self):
        # https://docs.python.org/ko/3/library/datetime.html#strftime-and-strptime-format-codes
        create_time = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        update_time = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"제목: {self.title}, 생성시간: {create_time}, 수정시간: {update_time}"
