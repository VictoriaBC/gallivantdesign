from django.contrib import admin
from .models import Illustration, Category

# Register your models here.

class IllustrationAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Illustration, IllustrationAdmin)
admin.site.register(Category, CategoryAdmin)