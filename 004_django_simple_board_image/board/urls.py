from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_create, name='post_create'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('upload_image/', views.upload_image, name='upload_image'),
]