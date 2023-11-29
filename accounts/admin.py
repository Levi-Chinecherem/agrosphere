from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

# Customize Django admin site details
admin.site.site_title = "AgroSphere Admin"
admin.site.site_header = "AgroSphere Admin"
admin.site.title = "AgroSphere Admin"
admin.site.header = "Welcome to AgroSphere Admin"
