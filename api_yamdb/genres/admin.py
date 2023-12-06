from django.contrib import admin

from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Genre._meta.fields]
