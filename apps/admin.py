from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin

from apps.models import Blog, BlogImages, Branch, Tag, Author


# Register your models here.

class BlogImagesTabularInline(TabularInline):
    model = BlogImages
    min_num = 1
    extra = 0


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    exclude = ('slug',)
    inlines = (BlogImagesTabularInline,)

#
# @admin.register(Category)
# class CategoryAdmin(ModelAdmin):
#     search_fields = ['name']
#     list_display = ['slug', 'name', 'id']
#     exclude = ('slug',)
#

@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ['slug', 'name', 'id']
    exclude = ('slug',)


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ['slug', 'name', 'id']
    exclude = ('slug',)

@admin.register(Author)
class TagAdmin(ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['slug', 'first_name','last_name', 'id']
    exclude = ('slug',)


# class CommentImageTabularInline(TabularInline):
#     model = BlogCommentImage
#     extra = 1
#
#
# @admin.register(BlogComment)
# class BlogAdmin(ModelAdmin):
#     exclude = ('updated_at',)
#     inlines = [CommentImageTabularInline]
