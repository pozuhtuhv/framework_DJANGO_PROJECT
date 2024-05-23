from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 특정 게시글 조회를 위한 URL
]
