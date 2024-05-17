from django.db import models
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=50)  # 제목 필드, 최대 50자
    writer = models.CharField(max_length=30)  # 작성자 필드, 최대 30자
    content = models.TextField()  # 내용 필드
    regdate = models.DateTimeField(auto_now_add=True)  # 등록 시간, 처음 저장 시에만 설정
    readcount = models.IntegerField(default=0)  # 조회수, 기본값 0

    def __str__(self):
        return f'{self.title}. {self.writer}({self.readcount})'

    def increment_readcount(self):
        self.readcount += 1
        self.save()
