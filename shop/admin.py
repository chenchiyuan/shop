# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from models import Region, Category, Shop, Product, ShopCategory
from models import Order, Item, Message
from models import User, WeiXin
from django.contrib.auth.models import Group
from models import Notice

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name", "region__name"]
    list_filter = ["region", ]
    list_display = ["name", "region", "priority"]

class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "telephone", "opentime", "address", "priority", "short_notice",  "sending_price", "image"]
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
    list_display = ["name", "shop", "category", "keywords"]

    def price_unit(self, obj):
        return obj.price_unit()
    price_unit.short_description = "单价"

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "shop":
            try:
                item = Product.objects.all().order_by('-id')[0]
                kwargs['initial'] = item.shop.id
            except:
                pass
        elif db_field.name == "category":
            try:
                item = Product.objects.all().order_by('-id')[0]
                kwargs['initial'] = item.category.id
            except:
                pass

        return super(ProductAdmin, self).formfield_for_foreignkey(
            db_field, request=request, **kwargs
        )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "unit":
            try:
                item = Product.objects.all().order_by('-id')[0]
                kwargs['initial'] = item.unit
            except:
                pass
        return super(ProductAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class OrderAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

class MyUserAdmin(admin.ModelAdmin):
    pass

class ShopCategoryAdmin(admin.ModelAdmin):
    pass

class NoticeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Region, RegionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ShopCategory, ShopCategoryAdmin)
admin.site.register(Notice, NoticeAdmin)

admin.site.register(User, MyUserAdmin)
