from django.contrib.auth import get_user_model
from django.db import models

# TODO: Define your user model here
User = get_user_model()


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name="friendships", on_delete=models.CASCADE)
    friend = models.ForeignKey(
        User, related_name="friends_of", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("user", "friend")
