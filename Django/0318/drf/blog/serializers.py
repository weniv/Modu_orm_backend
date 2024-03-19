from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"  # Test에서 사용하기 위해 모든 필드를 사용하도록 설정
