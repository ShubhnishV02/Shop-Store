from django.contrib import admin

# Register your models here.

from .models import Product, Category, Cart, Order, OrderItem, Profile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Cat_name','status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProdTitle','category', 'ProdName','selling_price','off_On_Product' , 'quantity','status','Unit','Net_Weight', 'created_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'Phone','City','Address','Pincode','payment_mode','payment_id', 'status']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product_name', 'price', 'quantity']

    def product_name(self, obj):
        return obj.product.ProdName
    product_name.short_description = "product_name"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Profile)
