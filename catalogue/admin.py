from django.contrib import admin

from .models import Category, MenuItem, Store, Option


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "store"]
    list_editable = ["store"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "alt_text",
        "slug",
        "is_available",
        "description",
        "created",
        "updated",
    ]
    list_filter = ["is_available"]
    list_editable = ["price", "alt_text", "is_available", "description"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "opening_hours", "closing_hours", "contact"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["opening_hours", "closing_hours", "contact"]


@admin.register(Option)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_editable = [
        "name",
        "price",
    ]
    list_display_links = None
