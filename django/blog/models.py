from django.db import models
from django.utils import timezone


class Post(models.Model): # 데이터베이스의 형태를 결정해주는 클래스로부터 상속
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE # 연결되어있는 로우가 사라질 경우 함께 사라짐
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    def publish(self):
        self.published_date = timezone.now()
        self.save() # 데이터베이스와 연동될때는 데이터베이스에 저장을 해줘야함.

    def __str__(self):
        return self.title
