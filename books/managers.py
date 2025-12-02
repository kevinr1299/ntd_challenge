from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q


class BookQuerySet(models.QuerySet):
    def liked_by_user_and_network(self, user):
        User = get_user_model()
        Like = ContentType.objects.get_by_natural_key("books", "like").model_class()

        network = [user.id]
        friends = User.objects.filter(
            Q(friendships__friend=user) | Q(friends_of__user=user)
        )
        network.extend(friends.values_list("id", flat=True))

        friends_of_my_friends = (
            User.objects.filter(
                Q(friendships__friend__in=friends) | Q(friends_of__user__in=friends)
            )
            .exclude(id=user.id)
            .distinct()
        )
        network.extend(friends_of_my_friends.values_list("id", flat=True))

        likes = (
            Like.objects.filter(
                content_type__model="book",
            )
            .filter(
                user_id__in=network,
            )
            .values_list("object_id", flat=True)
        )

        return self.filter(id__in=likes)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def liked_by_user_and_network(self, user):
        return self.get_queryset().liked_by_user_and_network(user)
