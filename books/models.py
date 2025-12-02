from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from books.managers import BookManager

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    objects = BookManager()


class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        unique_together = ("user", "content_type", "object_id")
