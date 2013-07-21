# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from shop.models.mixins import GetByUniqueMixin
from utils.alias import tran_lazy as _
from shop import const

class Region(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_region'
        verbose_name = verbose_name_plural = _('区域')

    name = models.CharField(_("区域名"), max_length=const.DB_NAME_LENGTH,
        help_text=_("每个公号一个区域名"))
    description = models.CharField(_("描述"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True)

    def __unicode__(self):
        return self.name

class Category(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = "shop"
        db_table = "shop_category"
        verbose_name = verbose_name_plural = _('分类')
        ordering = ["region", "-priority"]

    region = models.ForeignKey(Region, verbose_name=_("所属区域"))
    name = models.CharField(_("分类名"), max_length=const.DB_NAME_LENGTH)
    priority = models.IntegerField(_("优先级"), default=0, blank=True, null=True,
        help_text=u"数字越大优先级越高")

    def __unicode__(self):
        return "%s: %s" %(self.region, self.name)