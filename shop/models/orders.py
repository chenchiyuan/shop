# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from shop.models.shops import Shop
from shop.models.products import Product
from django.utils.timezone import now
from utils.alias import tran_lazy as _

class Order(models.Model):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_order'
        verbose_name = verbose_name_plural = _('订单')

    def __unicode__(self):
        return "%d: %s %s" %(self.id, self.shop, self.created_at.strftime("%Y-%m-%D %H:%M:%S"))

    shop = models.ForeignKey(Shop, verbose_name=_("商家"))
    created_at = models.DateTimeField(default=now, blank=True, null=True)
    total = models.FloatField(_("总价"), default=0.0, blank=True, null=True)

class Item(models.Model):
    class Meta:
        app_label = "shop"
        db_table = "shop_item"
        verbose_name = verbose_name_plural = _('物品')

    def __unicode__(self):
        return "%s: %d" %(self.product, self.quantity)

    product = models.ForeignKey(Product, verbose_name=_("商品"))
    quantity = models.IntegerField(_("数量"), default=0)

    order = models.ForeignKey(Order, verbose_name=_("账单"))
