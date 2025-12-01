from django.db import models


class Planet(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    population = models.BigIntegerField(
        null=True,
        blank=True,
    )
    terrains = models.BigIntegerField(
        null=True,
        blank=True,
    )
    climates = models.IntegerField(
        null=True,
        blank=True,
    )
