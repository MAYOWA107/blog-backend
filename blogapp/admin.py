from django.contrib import admin

from .models import CustomUser, Blog
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'bio', 'profile_picture', 'youtube']

admin.site.register(CustomUser, CustomUserAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_draft', 'category', 'author', 'created_at')

admin.site.register(Blog, BlogAdmin)