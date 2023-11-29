from django.db import models
from django.contrib.auth.models import User
from newsfeed.models import Post

class SharedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} shared {self.post.user.username}'s post"
