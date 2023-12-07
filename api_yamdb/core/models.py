from django.conf import settings
from django.db import models


class NameAndSlugModel(models.Model):
    name = models.CharField(max_length=settings.CHAR_NAME)
    slug = models.SlugField(
        max_length=settings.CHAR_SLUG,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.name[:settings.OUTPUT_LIMIT]

    class Meta:
        abstract = True
        ordering = ['name']
