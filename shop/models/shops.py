# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from shop.models.mixins import GetByUniqueMixin
from utils.alias import tran_lazy as _
from regions import Region, Category
from shop import const

class Shop(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_shop'
        verbose_name = verbose_name_plural = _('店铺')

    name = models.CharField(_("店名"), max_length=const.DB_NAME_LENGTH)
    owner = models.CharField(_("店主名"), max_length=const.DB_NAME_LENGTH,
        blank=True, null=True)
    phone = models.CharField(_("电话号码"), max_length=const.DB_PHONE_LENGTH,
        blank=True, null=True)
    address = models.CharField(_("地址"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True)
    notice = models.TextField(_("公告"), max_length=const.DB_NOTICE_LENGTH,
        blank=True, null=True, default="")
    picture = models.CharField(_("照片"), max_length=const.DB_NAME_LENGTH,
        blank=True, null=True, default=True)

    region = models.ForeignKey(Region, verbose_name=_("所属区域"))
    category = models.ForeignKey(Category, verbose_name=_("所属分类"), blank=True, null=True)

    def __unicode__(self):
        return "%s: %s: %s" %(self.region, self.owner, self.name)

