# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.utils import datetime_format
from utils.alias import tran_lazy as _
from django.db import models
from shop.models.regions import Region
from shop import const
from django.utils import timezone
from markdown import markdown

class Notice(models.Model):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_notice'
        verbose_name = verbose_name_plural = _('小区通知')
        ordering = ['-datetime']

    region = models.ForeignKey(Region, verbose_name=_("所属小区"))
    title = models.CharField(_("标题"), max_length=const.DB_NAME_LENGTH,
        blank=True, null=True, default="")

    content = models.TextField(_("内容"), max_length=const.DB_NOTICE_LENGTH,
        default="", blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __unicode__(self):
        return "%s: %s" %(self.region.name, self.content[:40])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.datetime = timezone.now()
        return super(Notice, self).save(force_insert=force_insert, force_update=force_update,
        using=using, update_fields=update_fields)

    @property
    def datetime_formatted(self):
        return datetime_format(self.datetime)

    @property
    def content_md(self):
        return markdown(self.content)