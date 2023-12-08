from django.contrib import admin

from categories.models import Category
from core.mixins import FieldListMixin


@admin.register(Category)
class CategoryAdmin(FieldListMixin, admin.ModelAdmin):
    pass
