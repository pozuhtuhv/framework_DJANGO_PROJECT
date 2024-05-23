from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)  # 필드 이름을 username으로 변경
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
