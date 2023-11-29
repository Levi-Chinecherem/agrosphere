# newsfeed/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
