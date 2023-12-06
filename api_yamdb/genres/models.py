from core.models import NameAndSlugModel


class Genre(NameAndSlugModel):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
