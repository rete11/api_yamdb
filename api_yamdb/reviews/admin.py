from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Review._meta.fields]
