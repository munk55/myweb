from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_data', 'published_data', 'category']
    fields = (('title', 'author'), 'body', 'images', 'excerpt', ('category', 'tags'))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
