from django.contrib import admin
from .models import Cart, Item


class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ['id', ]


class ItemAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'name', 'value', 'cart')
    search_fields = ['external_id', 'name', 'value']


admin.site.register(Cart, CartAdmin)
admin.site.register(Item, ItemAdmin)
