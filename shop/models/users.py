# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from shop.models.mixins import GetByUniqueMixin
from utils.alias import tran_lazy as _
from django.db import models
from django.utils import timezone
from shop import const
from managers import UserManager

class User(AbstractBaseUser, PermissionsMixin, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_user'
        verbose_name = verbose_name_plural = _('用户')

    token = models.CharField(
        verbose_name=_("Token"),
        max_length=255,
        unique=True,
        db_index=True
    )
    third_from = models.SmallIntegerField(_("来源"), choices=const.THIRD_FROM_CHOICES, default=const.LOCAL)

    email = models.CharField(_("邮箱"), max_length=128, default="", blank=True, null=True)
    username = models.CharField(_("姓名"), max_length=64, default="", blank=True, null=True)
    phone = models.CharField(_("手机"), max_length=const.DB_PHONE_LENGTH, blank=True, null=True)
    address = models.CharField(_("地址"), max_length=const.DB_ADDRESS_LENGTH, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "token"

    def __unicode__(self):
        return "%s: %s" %(self.get_third_from_display(), self.token)

    def get_full_name(self):
        return "%s: %s" %(self.get_third_from_display(), self.token)

    def get_short_name(self):
        return self.token

class WeiXin(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = "shop"
        db_table = "shop_weixin"
        verbose_name = verbose_name_plural = _('微信信息')

    token = models.CharField(
        verbose_name=_("Token"),
        max_length=255,
        unique=True,
        db_index=True
    )
    user = models.OneToOneField(User, verbose_name=_("用户"))
    joined_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __unicode__(self):
        return self.token
