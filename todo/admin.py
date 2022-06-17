from django.contrib import admin

from .models import Todo, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "content",
        "completed",
        "reminder",
        "created_at",
    )
