from django.contrib import admin
from .models import Product, Cart, Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "productid",
        "productname",
        "category",
        "description",
        "price",
        "image",
    ]

class CartAdmin(admin.ModelAdmin):
    list_display = ["userid","productid","qty"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["orderid","userid","productid","qty"]

admin.site.register(Product,ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order,OrderAdmin)