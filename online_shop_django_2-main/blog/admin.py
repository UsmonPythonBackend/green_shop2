from django.contrib import admin
from .models import BlogNews


@admin.register(BlogNews)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated')
    list_display_links = ('title', 'slug', 'created', 'updated')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
