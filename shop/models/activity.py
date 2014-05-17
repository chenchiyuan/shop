# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models
import time
from shop.models.mixins import GetByUniqueMixin


class Activity(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_activity'
        verbose_name = verbose_name_plural = u"活动"

    name = models.CharField(u"活动名称", max_length=128)
    owner = models.CharField(u"活动创建者", max_length=64, default="")
    description = models.CharField(u'活动描述', max_length=1024)

    def __unicode__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "times": map(lambda activity_time: activity_time.to_json(), list(self.activitytime_set.all())),
            "address:": map(lambda activity_address: activity_address.to_json(), list(self.activityaddress_set.all())),
        }


class ActivityTime(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_activity_time'
        verbose_name = verbose_name_plural = u"活动时间"
        ordering = ['-vote']

    activity = models.ForeignKey(Activity, verbose_name=u"所属活动")
    datetime = models.DateTimeField(u"活动时间")
    vote = models.IntegerField(u"支持票数", default=0)

    def __unicode__(self):
        return unicode(self.id)

    def to_json(self):
        return {
            "id": self.id,
            "activity_id": self.activity_id,
            "datetime": time.mktime(self.datetime.timetuple()),
            "vote": self.vote
        }


class ActivityAddress(models.Model, GetByUniqueMixin):
    class Meta:
        app_label = 'shop'
        db_table = 'shop_activity_address'
        verbose_name = verbose_name_plural = u"活动地点"
        ordering = ['-vote']

    activity = models.ForeignKey(Activity, verbose_name=u"所属活动")
    address = models.CharField(u"活动地点", max_length=256)
    vote = models.IntegerField(u"支持票数", default=0)

    def __unicode__(self):
        return unicode(self.id)

    def to_json(self):
        return {
            "id": self.id,
            "activity_id": self.activity_id,
            "address": self.address,
            "vote": self.vote
        }