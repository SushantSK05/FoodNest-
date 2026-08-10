from django.contrib import admin
from .models import Customer, Restaurant, Item, Cart, CartItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile', 'address')
    search_fields = ('username', 'email', 'mobile')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')
    list_filter = ('rating',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'vegeterian')
    list_filter = ('vegeterian', 'restaurant')
    search_fields = ('name', 'description')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'item', 'quantity')