from django.contrib import admin
from .models import Category, Comment, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'category']
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
