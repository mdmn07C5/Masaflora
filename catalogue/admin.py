from django.contrib import admin

from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'short_description', 'slug', 'is_available',
                    'full_description', 'created', 'updated']
    list_filter = ['is_available']
    list_editable = ['price', 'short_description', 'is_available',
                     'full_description']
    prepopulated_fields = {'slug': ('name',)}
