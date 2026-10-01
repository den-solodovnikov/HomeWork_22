from django.contrib import admin

from users.models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["is_superuser", "email", "phone", "country", "avatar"]
    list_filter = ("email",)
    search_fields = ("email", "phone")