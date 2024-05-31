from django.urls import path

from board.views import *

urlpatterns = [
    path('', post_create, name='post_create'),  # 루트 URL을 post_create 뷰로 매핑
    path('<str:title>/<int:pk>/', post_detail, name='post_detail'),  # 특정 게시글 조회를 위한 URL
]