# newsfeed/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'likes_count', 'image_preview')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'content')

    def likes_count(self, obj):
        return obj.likes.count()

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />'
        return None

    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
