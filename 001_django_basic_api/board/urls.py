from django.urls import path

from . import views

urlpatterns = [
    path('board/', views.BoardListCreate.as_view(), name='board-list-create'),
    path('board/<int:pk>/', views.BoardDetail.as_view(), name='board-detail'),
]