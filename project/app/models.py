import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy


class Director(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, max_length=128, blank=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return str(self.name) + " (" + str(self.id) + ")"


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(
        null=False,
        max_length=128,
        blank=False,
    )
    year = models.IntegerField(null=True)
    directors = models.ManyToManyField(Director)

    class Meta:
        ordering = ["year", "title"]
        verbose_name = "Film"
        verbose_name_plural = "Films"

    def __str__(self):
        return str(self.title) + " (" + str(self.id) + ")"