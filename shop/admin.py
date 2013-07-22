# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from models import Region, Category, Shop, Product
from models import Order, Item, Message

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name", "region__name"]
    list_filter = ["region", ]
    list_display = ["name", "region", "priority"]

class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "telephone", "opentime", "address", "short_notice", "sending_price", "image"]
    search_fields = ["name", "owner"]

    def telephone(self, obj):
        return obj.telephone()
    telephone.short_description = "电话"

    def opentime(self, obj):
        return obj.opentime()
    opentime.short_description = "营业时间"

    def short_notice(self, obj):
        return obj.notice[:40]
    short_notice.short_description = "简短公告"

    def image(self, obj):
        return '<img href="%s">' % obj.picture
    image.short_description = "图片"
    image.allow_tags = True


class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", "keywords", "shop__name"]
    list_display = ["name", "shop", "price_unit", "category", "keywords"]

    def price_unit(self, obj):
        return obj.price_unit()
    price_unit.short_description = "单价"

class OrderAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Region, RegionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Message, MessageAdmin)