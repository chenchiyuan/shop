# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from shop.weixin.weixin import WeiXin
from shop.models import Region
from utils.helper import get_url_by_conf, get_domain_path
from shop import const

class WeiXinView(View):
    def get(self, request, *args, **kwargs):
        echostr = request.GET.get("echostr", "")
        return HttpResponse(echostr)

    def post(self, request, *args, **kwargs):
        w = WeiXin.on_message(request.body)
        json_data = w.to_json()
        token = json_data['FromUserName']

        region = Region.get_by_unique(**kwargs)
        notices_url = get_url_by_conf("region_notices", args=[region.id])
        categories = region.category_set.all()[:8]
        articles = [
            {
                "title": u"%s公告栏" % region.name,
                "description": u"%s" %region.description,
                "picurl": "http://life.zoneke.com/static/assets/community/logo.jpg",
                "url": const.auto_login_url(notices_url, token=token)
            }
        ]
        for category in categories:
            url = get_domain_path(get_url_by_conf("region_category", args=[region.id, category.id]))
            article = {
                "title": category.name,
                "description": "",
                "picurl": const.ARROW_IMAGE,
                "url": const.auto_login_url(url, token=token)
            }
            articles.append(article)

        xml = w.to_pic_text(from_user_name=json_data['ToUserName'], to_user_name=json_data['FromUserName'],
            articles=articles)
        return HttpResponse(xml)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WeiXinView, self).dispatch(request, *args, **kwargs)