# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from shop.models import Shop

class CategoryShopsView(TemplateView):
    template_name = "shops.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryShopsView, self).get_context_data(**kwargs)
        shops = Shop.filter_by_queries(**kwargs)
        context['shops'] = shops
        return context


