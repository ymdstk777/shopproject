# shop/admin.py
from django.contrib import admin
from .models import Category, ShopPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # 'title'はCategoryモデルに存在
    list_display_links = ('id', 'title')

class ShopPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # 'title'はShopPostモデルに存在
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopPost, ShopPostAdmin)