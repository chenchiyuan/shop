# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from shop.models import Shop
from utils.alias import tran_lazy as _
from shop import const

class Product(models.Model):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_product'
        verbose_name = verbose_name_plural = _('商品')

    name = models.CharField(_("商品名"), max_length=const.DB_NAME_LENGTH)
    price = models.IntegerField(_("单价"), default=0)
    unit = models.CharField(_("单位"), max_length=8, default="个", blank=True, null=True)

    shop = models.ForeignKey(Shop, verbose_name=_("商户"))
    keywords = models.CharField(_("搜索关键字"), blank=True, null=True, default="",
        help_text=u"搜索关键字", max_length=const.DB_NAME_LENGTH)
    category = models.CharField(_("商品分类"), blank=True, null=True,
        default="", max_length=const.DB_NAME_LENGTH)

    picture = models.CharField(_("照片"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True, default="")

    def __unicode__(self):
        return "%s: %s" %(self.shop.name, self.name)

    def price_unit(self):
        return "%d元/ %s" %(self.price, self.unit)