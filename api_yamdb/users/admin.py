from django.contrib import admin
from django.contrib.auth import get_user_model


CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'bio',
    )
    search_fields = ('username', 'role',)
    list_filter = ('username',)
