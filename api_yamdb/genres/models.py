from django.db import models


class Genre(models.Model):
    name = models.CharField(
        'имя жанра',
        max_length=254,
    )
    slug = models.SlugField(
        'cлаг жанра',
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name} {self.name}'
