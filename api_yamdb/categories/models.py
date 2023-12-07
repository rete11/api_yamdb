from core.models import NameAndSlugModel


class Category(NameAndSlugModel):
    class Meta(NameAndSlugModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
