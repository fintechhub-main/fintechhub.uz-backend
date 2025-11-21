from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=96)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    video = models.FileField(upload_to="blog_videos/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
