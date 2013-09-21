# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from interface import StateInterface
from shop import const
from shop.models import Region
from utils.helper import get_url_by_conf, get_domain_path
from datetime import datetime

INDEX = "INDEX"
AFTER_SUBSCRIBE = "AFTER_SUBSCRIBE"

class StateIndex(StateInterface):
    def to_xml(self):
        ignore = self.ignore
        if ignore:
            return self._to_wx_text()

        token = self.to_user_name

        region = Region.get_by_unique(id=self.region_id)
        notices_url = get_url_by_conf("region_notices", args=[region.id])
        categories = region.category_set.all()[:7]
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

        articles.append({
            "title": "回复m获取最新菜单\n(当前版本%s)" %datetime.now().strftime("%Y-%m-%d") ,
            "description": "",
            "picurl": "",
            "url": ""
            }
        )
        return self._to_full_text(articles)

    def handle(self, content):
        if content.lower() == "m":
            return INDEX, {
                "region_id": self.region_id,
                "ignore": False
            }
        else:
            return INDEX, {
                "region_id": self.region_id,
                "ignore": True
            }

class StateAfterSubscribe(StateIndex):
    def to_xml(self):
        content = "欢迎关注北纬40生活小帮手" \
                  "回复m获取最新菜单"
        return self._to_wx_text(content)