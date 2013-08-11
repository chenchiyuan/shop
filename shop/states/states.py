# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from interface import StateInterface
from shop import const
from shop.models import Region
from utils.helper import get_url_by_conf, get_domain_path

INDEX = "INDEX"
AFTER_SUBSCRIBE = "AFTER_SUBSCRIBE"

class StateIndex(StateInterface):
    def to_xml(self):
        ignore = self.meta.get("ignore", True)
        if ignore:
            return self._to_wx_text()

        token = self.to_user_name

        region = Region.get_by_unique()
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
            "title": "请回复m获取最新的菜单",
            "description": "",
            "picurl": "",
            "url": ""
            }
        )
        return self._to_full_text(articles)

    def handle(self, content):
        if content.lower == "m":
            return INDEX, {"region_id": self.meta.get("region_id", 1),
                           "ignore": False
            }
        else:
            return INDEX, {"region_id": self.meta.get("region_id", 1),
                           "ignore": True
            }

class StateAfterSubscribe(StateIndex):
    def to_xml(self):
        content = "欢迎关注北纬40生活小帮手" \
                  "回复m获取最新的菜单"
        return self._to_wx_text(content)