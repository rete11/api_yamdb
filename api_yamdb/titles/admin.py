from django.contrib import admin

from titles.models import Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Title._meta.fields]
