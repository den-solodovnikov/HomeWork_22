from django.contrib import admin
from catalog.models import Category, Product, Contact


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
