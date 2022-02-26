from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField

class OrderItem_Admin(admin.TabularInline):
    model = Order_Item
    list_dispaly = ['product','quantity']
    extra = 0

class Order_Admin(admin.ModelAdmin):
    inlines = [OrderItem_Admin]


admin.site.register(Order,Order_Admin)
admin.site.register(Shipping_Adress)
admin.site.register(Wishlist)