from django.contrib import admin

from reviews.models import Review
from core.mixins import FieldListMixin


@admin.register(Review)
class ReviewAdmin(FieldListMixin, admin.ModelAdmin):
    pass
