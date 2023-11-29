# chat/models.py

from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    members = models.ManyToManyField(User)
    image = models.ImageField(upload_to='group_images/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ManyToManyField(User, related_name='admin_groups', blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='chat_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} in {self.group.name}' if self.group else f'{self.sender.username} to {self.recipient.username}'
