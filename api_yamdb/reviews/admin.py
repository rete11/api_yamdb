from django.contrib import admin

from core.mixins import FieldListMixin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(FieldListMixin, admin.ModelAdmin):
    pass
