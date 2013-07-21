# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from shop.models import Shop, Category

class CategoryShopsView(TemplateView):
    template_name = "shop/shops.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryShopsView, self).get_context_data(**kwargs)
        category_id = kwargs.get("category_id", 0)
        category = Category.get_by_unique(id=category_id)
        shops = category.shop_set.all()
        context['shops'] = shops
        context['category'] = category
        return context


