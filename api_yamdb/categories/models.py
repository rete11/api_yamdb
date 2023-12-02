from django.db import models


class Category(models.Model):
    name = models.CharField(
        'имя категории',
        max_length=254,
    )
    slug = models.SlugField(
        'слаг категории',
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} {self.name}'
