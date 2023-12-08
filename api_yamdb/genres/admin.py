from django.contrib import admin

from core.mixins import FieldListMixin
from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(FieldListMixin, admin.ModelAdmin):
    pass
