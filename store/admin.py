from django.contrib import admin

# Register your models here.

from .models import Product, Category, Cart

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Cat_name','status']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
