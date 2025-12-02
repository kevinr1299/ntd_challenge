from django.contrib import admin

from books.models import Book, Like


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "content_type",
        "object_id",
    )
