from django.contrib import admin

from blogs.models import Blog
from catalog.models import Category, Product, Contact
from users.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ("name", "description")


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "message"]
    search_fields = ("name", "phone")


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image", "content", "is_published", "views_counter", "is_notification_sent"]
    list_filter = ("is_published", "title",)
    search_fields = ("title", "content")

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["is_superuser", "email", "phone", "country", "avatar"]
    list_filter = ("email",)
    search_fields = ("email", "phone")