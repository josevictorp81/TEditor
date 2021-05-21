from django.contrib import admin

from .models import Text, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'create', 'update']
    search_fields = ['title',]
