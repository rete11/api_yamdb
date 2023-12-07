from django.contrib import admin

from core.mixins import FieldListMixin
from titles.models import Title


@admin.register(Title)
class TitleAdmin(FieldListMixin, admin.ModelAdmin):
    pass
