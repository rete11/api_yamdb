from django.contrib import admin

from genres.models import Genre
from core.mixins import FieldListMixin


@admin.register(Genre)
class GenreAdmin(FieldListMixin, admin.ModelAdmin):
    pass
