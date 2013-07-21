# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

class OrdersView(View):
    def get(self, request, *args, **kwargs):
        return

    def post(self, request, *args, **kwargs):
        return

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrdersView, self).dispatch(request, *args, **kwargs)