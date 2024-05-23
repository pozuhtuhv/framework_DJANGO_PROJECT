from django.contrib import admin
from django.urls import path
from board import views  # board 앱의 뷰를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),  # 루트 URL에 post_list 뷰를 매핑
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 특정 게시글 조회를 위한 URL
]
