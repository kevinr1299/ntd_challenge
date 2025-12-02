from django.contrib import admin

from users.models import Friendship


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "friend",
    )
