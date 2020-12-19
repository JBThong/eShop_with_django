from django.contrib import admin
from .models import Product, Category, User, Order, OrderDetail

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'stock', 'cate_id']

class AdminCate(admin.ModelAdmin):
    list_display = ['name']

# class AdminOrder(admin.ModelAdmin):
#     list_display = ['product', 'phone', 'quantity']

class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'phone', 'password']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCate)
admin.site.register(User, AdminUser)
admin.site.register(Order)
admin.site.register(OrderDetail)