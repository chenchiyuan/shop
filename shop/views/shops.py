# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from shop.models import Shop

class ShopDetailView(TemplateView):
    template_name = "shop_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        shop_id = kwargs.get("shop_id", "")
        shop = Shop.get_by_unique(id=shop_id)
        context['shop'] = shop
        return context