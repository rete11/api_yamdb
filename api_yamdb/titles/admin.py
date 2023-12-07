from django.contrib import admin

from titles.models import Title
from core.mixins import FieldListMixin


@admin.register(Title)
class TitleAdmin(FieldListMixin, admin.ModelAdmin):
    pass
