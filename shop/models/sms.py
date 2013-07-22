# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
from utils.alias import tran_lazy as _
from shop.models.orders import Order
from shop import const
from utils.sms import sender
import json

class Message(models.Model):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_message'
        verbose_name = verbose_name_plural = _('短信')

    sender = models.CharField(_("买家"), max_length=const.DB_NAME_LENGTH)
    phone = models.CharField(_("买家手机"), max_length=const.DB_PHONE_LENGTH)
    to = models.CharField(_("商家手机"), max_length=const.DB_PHONE_LENGTH)
    order = models.ForeignKey(Order, verbose_name=_("订单"))

    success = models.BooleanField(_("状态"), default=True)
    content = models.CharField(_("短信内容"), max_length=const.DB_MESSAGE_LENGTH,
        blank=True, null=True, default="")
    response = models.CharField(_("返回码"), max_length=const.DB_ADDRESS_LENGTH,
        blank=True, null=True, default="", help_text="平台返回的内容，用于调试")

    def __unicode__(self):
        return "%s %s => %s" %(self.sender, self.phone, self.to)

    def send(self):
        if not self.order.item_set.count():
            return False

        to = self.order.shop.phone
        self.to = to

        header = "%s %s\n" %(self.sender, self.phone)
        items = []
        total = 0
        for item in self.order.item_set.all():
            items.append("%s*%d" %(item.product.name, item.quantity))
            total += item.quantity*item.product.price
        body = " ".join(items)
        footer = "\n总价:%d" %total

        content = header + body + footer
        res, success = sender(self.to, content)
        response = json.dumps(res.content)
        success = True
        response = '{"result": 1}'

        self.content = content
        self.response = response
        self.success = success
        self.save()
        return True