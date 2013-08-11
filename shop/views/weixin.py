# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from shop.weixin.receiver import WeiXinReceiver

class WeiXinView(View):
    def get(self, request, *args, **kwargs):
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)

    def post(self, request, *args, **kwargs):
        content = request.body
        state = WeiXinReceiver.get_state(content, **kwargs)
        xml_data = state.to_xml()
        return HttpResponse(xml_data)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WeiXinView, self).dispatch(request, *args, **kwargs)