from core.models import NameAndSlugModel


class Genre(NameAndSlugModel):

    class Meta(NameAndSlugModel.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
