from django.contrib import admin
from goods.models import Categories, Products

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    pass


class ProductsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
