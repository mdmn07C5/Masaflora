from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Category, MenuItem, Store, Option


class OptionsInline(admin.TabularInline):
    model = Option.item.through


class OptionsCategoryInline(admin.TabularInline):
    model = Option.category.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "store"]
    list_editable = ["store"]
    inlines = [
        OptionsCategoryInline,
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    inlines = [
        OptionsInline,
    ]
    list_display = [
        "name",
        "price",
        "alt_text",
        "slug",
        "category",
        "is_available",
        "description",
        "created",
        "updated",
    ]
    list_filter = ["is_available"]
    list_editable = ["price", "alt_text", "is_available", "description"]

    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "10"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 1, "cols": 40})},
    }
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "opening_hours", "closing_hours", "contact"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["opening_hours", "closing_hours", "contact"]


@admin.register(Option)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    list_editable = ["name", "price"]
    list_display_links = None
