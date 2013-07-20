# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from shop.views.categories import CategoryShopsView
from shop.views.shops import ShopDetailView
from shop.views.weixin import WeiXinView
import const

urlpatterns = patterns('',
    url(r'^regions/%s/weixin/$' %const.URL_ID, WeiXinView.as_view(), name="weixin_api"),
    url(r'^regions/%s/categories/%s/$' %(const.URL_REGION_ID, const.URL_CATEGORY_ID), CategoryShopsView.as_view(),
        name="region_category"),
    url(r'^regions/%s/shops/%s/$' %(const.URL_REGION_ID, const.URL_SHOP_ID), ShopDetailView.as_view(), name="region_shop"),
    #url(r'^regions/%s/shops/%s/notice/$' %(const.URL_REGION_ID, const.URL_SHOP_ID), "", name="region_shop_notice"),
)
