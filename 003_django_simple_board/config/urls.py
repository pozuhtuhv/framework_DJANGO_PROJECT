from board import views  # board 앱의 뷰를 임포트
from django.urls import path

urlpatterns = [
    path('', views.post_create, name='post_create'),  # 루트 URL에 post_create 뷰를 매핑
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 특정 게시글 조회를 위한 URL
]
