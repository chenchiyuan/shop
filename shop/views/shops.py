# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from shop.models import Shop

class ShopDetailView(TemplateView):
    template_name = "shop/shop_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        shop_id = kwargs.get("shop_id", "")
        shop = Shop.get_by_unique(id=shop_id)
        context['shop'] = shop
        filter = "true"
        if not shop.product_set.count():
            filter = "false"
        context['filter'] = filter

        return context

class ShopNoticeView(View):
    def get(self, requests, *args, **kwargs):
        shop_id = kwargs.get("shop_id", "")
        shop = Shop.get_by_unique(id=shop_id)
        return HttpResponse(shop.notice_md)
