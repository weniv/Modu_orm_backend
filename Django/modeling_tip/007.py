# modeling_tip/007.py
# 모델 인스턴스의 변경 이력을 기록할 수 있습니다.
# action_time: 액션이 발생한 시간
# user: 액션을 수행한 사용자
# content_type: 변경된 모델의 ContentType
# object_id: 변경된 객체의 프라이머리 키
# object_repr: 변경된 객체의 문자열 표현
# action_flag: 수행된 액션의 종류 (추가, 변경, 삭제 등)
# change_message: 변경 내용에 대한 설명

from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    # ...
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        LogEntry.objects.log_action(
            user_id=None,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=self.pk,
            object_repr=str(self),
            action_flag=CHANGE,
            change_message=f"Post {self.pk} has been updated.",
        )


# 모든 로그를 조회합니다.
from django.contrib.admin.models import LogEntry

logs = LogEntry.objects.all()
for log in logs:
    print(
        log.action_time, log.user, log.content_type, log.object_repr, log.change_message
    )
