# newsfeed/urls.py
from django.urls import path
from .views import (
    feed_details,
    create_post,
    news_feed,
    share_post,
    profile_details,
    toggle_like,
    delete_post,
    like_post,
    update_post,
)

urlpatterns = [
    path('news-feed/', news_feed, name='feed'),
    path('profile-details/<int:user_id>/', profile_details, name='profile_details'),
    path('toggle-like/', toggle_like, name='toggle_like'),
    path('create/', create_post, name='create_post'),
    path('sharing/share-post/<int:post_id>/', share_post, name='share_post'),
    path('feed-details/<int:post_id>/', feed_details, name='feed_details'),
    path('delete-post/<int:post_id>/', delete_post, name='delete_post'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
    path('update-post/<int:post_id>/', update_post, name='update_post'),
]
