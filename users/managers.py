from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

User = get_user_model()


class FriendshipQuerySet(models.QuerySet):
    def get_friends(self, user):
        return User.objects.filter(
            Q(friendships__user=user) | Q(friends_of__friend=user)
        )


class FriendshipManager(models.Manager):
    def get_queryset(self):
        return FriendshipQuerySet(self.model, using=self._db)

    def get_friends(self, user):
        return self.get_queryset().get_friends(user)
