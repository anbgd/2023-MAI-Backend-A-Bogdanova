import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy


def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, max_length=128, blank=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return str(self.name) + " (" + str(self.id) + ")"


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(
        null=False,
        max_length=128,
        blank=False,
    )
    year = models.IntegerField(null=True, validators=[validate_positive])
    countries = models.ManyToManyField(Country)

    class Meta:
        ordering = ["title"]
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return str(self.title) + " (" + str(self.id) + ")"