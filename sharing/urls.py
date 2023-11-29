from django.urls import path
from .views import shared_items, share_post

urlpatterns = [
    path('shared-items/', shared_items, name='shared_items'),
    path('share-post/<int:post_id>/', share_post, name='share_post'),
]
