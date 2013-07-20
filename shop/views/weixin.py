# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from shop.weixin.weixin import WeiXin
from shop.models import Region

class WeiXinView(View):
    def get(self, request, *args, **kwargs):
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)

    def post(self, request, *args, **kwargs):
        region = Region.get_by_unique(**kwargs)
        categories = region.category_set.all()[:8]
        articles = [
            {
                "title": u"%s" % region.name,
                "description": u"%s" %region.description,
                "picurl": "http://cayman.b0.upaiyun.com/71509cef7a4940aea89fa6d512be8715.jpeg!medium",
                "url": ""
            }
        ]
        for category in categories:
            article = {
                "title": category.name,
                "description": "",
                "picurl": "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-go-next-icon.png",
                "url": ""
            }
            articles.append(article)

        w = WeiXin.on_message(request.body)
        json_data = w.to_json()
        xml = w.to_pic_text(from_user_name=json_data['ToUserName'], to_user_name=json_data['FromUsername'],
            articles=articles)
        return HttpResponse(xml)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WeiXinView, self).dispatch(request, *args, **kwargs)