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
        ordering = ['-priority']

    name = models.CharField(_("店名"), max_length=const.DB_NAME_LENGTH)
    owner = models.CharField(_("店主名"), max_length=const.DB_NAME_LENGTH,
        blank=True, null=True)
    phone = models.CharField(_("电话号码"), max_length=const.DB_PHONE_LENGTH,
        blank=True, null=True)
    phone2 = models.CharField(_("电话号码2"), max_length=const.DB_PHONE_LENGTH,
        blank=True, null=True)

    start = models.TimeField(_("营业开始时间"), default=None, blank=True,
        null=True, help_text=_(""))
    end = models.TimeField(_("营业结束时间"), default=None, blank=True,
        null=True, help_text=_(""))

    address = models.CharField(_("地址"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True)

    intro = models.TextField(_("简短公告"), max_length=const.DB_MESSAGE_LENGTH,
        default="", blank=True, null=True,
        help_text=_("简短公告, 用于列表页面展示"))

    notice = models.TextField(_("公告"), max_length=const.DB_NOTICE_LENGTH,
        blank=True, null=True, default="")

    picture = models.CharField(_("照片"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True, default="")

    priority = models.IntegerField(_("优先级"), default=0, blank=True, null=True,
        help_text=u"数字越大优先级越高")

    sending_price = models.SmallIntegerField(_(u"起送价格"), default=0,
        blank=True, null=True)

    region = models.ForeignKey(Region, verbose_name=_("所属区域"))
    category = models.ForeignKey(Category, verbose_name=_("所属分类"), blank=True, null=True)

    def __unicode__(self):
        return "%s: %s: %s" %(self.region, self.owner, self.name)

    def get_picture(self):
        if self.picture:
            return self.picture
        else:
            return const.SHOP_PICTURE_DEFAULT

    def opentime(self):
        if not self.start and not self.end:
            return u"全天开业"
        else:
            return "%s 至 %s" % (self.start.strftime("%H:%M"), self.end.strftime("%H:%M"))

    def telephone(self):
        phones = []
        if self.phone:
            phones.append(self.phone)
        if self.phone2:
            phones.append(self.phone2)
        return ",".join(phones)

class ShopCategory(models.Model):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_shop_category'
        verbose_name = verbose_name_plural = _('店铺分类')

    shop = models.ForeignKey(Shop, verbose_name=_("商铺"))
    name = models.CharField(_("分类名"), max_length=const.DB_NAME_LENGTH)
    priority = models.IntegerField(_("优先级"), default=0, blank=True, null=True,
        help_text=u"数字越大优先级越高")

    def __unicode__(self):
        return "%s: %s" %(self.shop.name, self.name)