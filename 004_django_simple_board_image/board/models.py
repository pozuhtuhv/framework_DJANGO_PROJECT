import os
from django.db import models
from datetime import datetime

def get_image_filename(instance, filename):
    now = datetime.now()
    return os.path.join('images', now.strftime('%Y%m%d%H%M%S') + os.path.splitext(filename)[1])

class Board(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to=get_image_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url
