from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    OCCUPATION_CHOICES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    occupation = models.CharField(max_length=10, choices=OCCUPATION_CHOICES)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    communicated_users = models.ManyToManyField(User, related_name='communicated_users', blank=True)
    
    def __str__(self):
        return self.full_name
