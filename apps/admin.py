from django.contrib import admin

from apps.models import Branch, Category, Tag, Blog

# Register your models here.
admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
