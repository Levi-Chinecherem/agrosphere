# chat/admin.py

from django.contrib import admin
from .models import Group, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ['name']

admin.site.register(Group, GroupAdmin)
admin.site.register(Message)
