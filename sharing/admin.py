from django.contrib import admin
from .models import SharedItem

class SharedItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'shared_at')
    list_filter = ('user', 'post')
    search_fields = ('user__username', 'post__user__username')
    date_hierarchy = 'shared_at'

admin.site.register(SharedItem, SharedItemAdmin)
